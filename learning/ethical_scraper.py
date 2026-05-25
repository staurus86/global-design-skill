# learning/ethical_scraper.py
"""Ethical HTTP client with robots.txt compliance and rate limiting."""
import time
import urllib.robotparser
from urllib.parse import urlparse

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

USER_AGENT = "GlobalDesignSkill-Bot/1.0 (Learning/Reference Collection)"
RATE_LIMIT_SECONDS = 6  # 10 requests/minute = 1 per 6 seconds


class EthicalScraper:
    def __init__(self):
        self._robots_cache: dict[str, urllib.robotparser.RobotFileParser] = {}
        self._last_request_time: float = 0.0

    def can_fetch(self, url: str) -> bool:
        """Check robots.txt before fetching."""
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        robots_url = f"{base}/robots.txt"

        if base not in self._robots_cache:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(robots_url)
            try:
                rp.read()
            except Exception:
                rp = None
            self._robots_cache[base] = rp

        rp = self._robots_cache[base]
        if rp is None:
            return True  # Cannot read robots.txt — allow
        return rp.can_fetch(USER_AGENT, url)

    def fetch(self, url: str) -> dict:
        """Fetch a URL respecting robots.txt and rate limits.

        Returns: {"html": str, "url": str, "status": int} or {"error": str}
        """
        if not REQUESTS_AVAILABLE:
            return {"error": "requests library not installed. Run: pip install requests"}

        if not self.can_fetch(url):
            return {"error": f"Disallowed by robots.txt: {url}"}

        elapsed = time.time() - self._last_request_time
        if elapsed < RATE_LIMIT_SECONDS:
            time.sleep(RATE_LIMIT_SECONDS - elapsed)

        try:
            response = requests.get(
                url,
                headers={"User-Agent": USER_AGENT},
                timeout=10,
            )
            self._last_request_time = time.time()
            return {
                "html": response.text,
                "url": url,
                "status": response.status_code,
            }
        except requests.RequestException as e:
            return {"error": str(e)}
