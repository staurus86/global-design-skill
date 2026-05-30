# Golden output — o04: patient appointment booking (health sector)

**Prompt:** "Use global-design-skill and design a patient appointment booking flow for a private clinic."

---

## What a correct response must include

### 1. Sector auto-detection

Must detect the **health** sector from "patient", "clinic", "appointment" and load sector rules (`GlobalDesignSkill:get_sector_context` / `industries/health.md`) — without the user naming the sector.

### 2. Trust-first hierarchy

Must lead with `trust`, not conversion pressure:
- Clinic credentials, `certification`/licensing, and named practitioners surfaced early
- Reassurance about data handling before asking for personal details

### 3. Privacy and sensitive data

Must address `privacy`: what data is collected, why, and a visible consent/privacy statement at the point of entry. Health data is sensitive by default.

### 4. The appointment flow itself

Must specify the `appointment` booking steps: choose service → choose `doctor`/practitioner → choose slot → confirm. Each step with loading, empty (no slots), and error states.

### 5. Doctor selection

Must let the patient pick or be matched to a `doctor`, with specialty, availability, and enough credibility signal to choose confidently.

### 6. Gate compliance

Must satisfy Gates 1–5 (problem, IA, design system, states, responsive), with the booking flow mapped entry → task → outcome.

---

## What a correct response must NOT include

(Banned for the health sector — see `industries/health.md`)

- `aggressive CTA` language ("Book NOW or lose your spot")
- `flash sale` / discount-pressure framing on care
- `countdown timer` urgency mechanics on appointment slots
- Conversion dark patterns that override patient trust
