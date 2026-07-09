This replaces the previous Restart Packet and reflects the current architectural baseline after today's milestone.

# 🔥 PREPFLOW RESTART PACKET v3 (COPY/PASTE ONLY)

## PROJECT STATUS

PrepFlow has completed the transition from a proof-of-concept architecture to a coordinated Source Module pipeline.

GitHub is the source of truth.

Latest milestone has been committed and pushed.

---

# CURRENT ARCHITECTURE

```
Original Source (PDF)
        │
        ▼
Extract
        │
        ▼
Clean / Normalize
        │
        ▼
Parse
        │
        ▼
Canonical Source Module
        │
        ▼
Everything Else
```

PrepFlow is a compiler.

It is **not** a quiz engine.

Quiz generation is simply one consumer of the compiled source modules.

Do not redesign this architecture unless an actual conflict is discovered through implementation.

---

# CURRENT PIPELINE STATUS

## Stage 1 — Extract

**Status:** ✅ COMPLETE

Implemented:

```
tools/extract_text.py
```

Responsibilities:

* Read the original PDF.
* Preserve text faithfully.
* Do not clean.
* Do not interpret.
* Do not parse.

Current output:

```
scratch/pharm_raw.txt
```

Verified using the original Pharmacy PDF.

---

## Stage 2 — Clean / Normalize

**Status:** ✅ WORKING

Implemented:

```
tools/clean_pharm_text.py
```

Responsibilities:

* Remove publisher noise.
* Remove advertisements.
* Remove repeated headers/footers.
* Remove page artifacts.
* Normalize formatting.
* Preserve all educational content.

Current output:

```
scratch/pharm_clean.txt
```

---

## Stage 3 — Parse

**Status:** ✅ WORKING

Implemented:

```
tools/parse_pharm_module.py
```

Responsibilities:

* Detect questions.
* Detect answers.
* Detect rationales.
* Build structured question objects.

Current verified output:

```
1085 Pharmacy questions
```

Preview file:

```
scratch/pharm_module_preview.json
```

---

## Stage 4 — Write Source Module

**Status:** ⏳ PLACEHOLDER

This is now the next implementation target.

Responsibilities:

* Take parsed question objects.
* Write the canonical PrepFlow Source Module.
* No parsing logic belongs here.
* No extraction logic belongs here.

---

# SOURCE MODULE BUILDER

Current orchestrator:

```
tools/build_source_module.py
```

Current execution flow:

```
Extract
↓
Clean
↓
Parse
↓
Write
```

Extract, Clean, and Parse are now real stages.

Write remains the only placeholder.

---

# VERIFIED MILESTONE

The original Pharmacy PDF now successfully runs through the new pipeline:

```
Original Pharmacy PDF
        ↓
extract_text.py
        ↓
scratch/pharm_raw.txt
        ↓
clean_pharm_text.py
        ↓
scratch/pharm_clean.txt
        ↓
parse_pharm_module.py
        ↓
1085 parsed questions
        ↓
Preview JSON
```

Artifacts verified:

* `scratch/pharm_raw.txt`
* `scratch/pharm_clean.txt`
* `scratch/pharm_module_preview.json`

This end-to-end pipeline has been committed and pushed.

---

# MIGRATION STRATEGY (LOCKED)

Do **not** rewrite working prototypes.

Instead:

1. Build reusable modules.
2. Route the pipeline through them.
3. Verify identical behavior.
4. Commit.
5. Push.
6. Retire prototype code only after replacement is fully validated.

Risk reduction takes priority over elegance.

---

# DO NOT DO YET

Do not delete:

* Existing importer scripts.
* Existing compiler code.
* Existing source representations.
* Prototype implementations.

Deletion is a validation milestone—not an implementation step.

The old code remains the reference implementation until the new pipeline produces equivalent canonical output for both supported sources.

---

# DEVELOPMENT DISCIPLINE

For every implementation step:

1. Observe.
2. Inspect existing code.
3. Make one focused change.
4. Run.
5. Verify.
6. Commit.
7. Push.
8. Perform a top-down review.
9. Continue.

Avoid speculative redesigns.

Avoid logic loops.

Keep a separate ranked list of future ideas instead of interrupting implementation unless an idea prevents the current work.

---

# CURRENT PRIORITY

Complete the remaining pipeline stage:

```
Write Source Module
```

After that:

1. Verify the canonical Pharmacy Source Module.
2. Run the identical pipeline on the original Medical-Surgical PDF.
3. Modify downstream stages only if evidence requires source-specific handling.

---

# PROJECT FOCUS

Current objective is **not** adding more sources.

Current objective is **not** adding more features.

Current objective is to finish one complete compiler pipeline capable of producing canonical source modules from the two validated source banks:

* Pharmacy
* Medical-Surgical

Everything else builds on that foundation.

---

# FIRST TASK WHEN RESTARTING

1. Read this packet.
2. Perform a top-down review against the current GitHub repository.
3. Confirm architecture matches this document.
4. Continue implementing the Write Source Module stage.
5. Validate output.
6. Commit.
7. Push.

This version should serve as the new baseline until we complete the Write stage or encounter an architectural change significant enough to warrant a new restart packet.
