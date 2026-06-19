# GLOSSARY.md — ADOS Quality Drift Auditor v0.2

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | glossary |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | semantic_authority |
| GOVERNANCE_AREA | glossary; project; quality |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use before interpreting any Project, input surface, Metric, Archetype, Domain, Problem Pattern, schema, or report. |
| HOW_TO_USE | Retrieve relevant term records by ID and use their definitions, boundaries, relationships, auditor use, and drift checks. Other files may reference these terms but must not redefine them. |
| DOCUMENT_CONTENT | Primary ADOS-specific concept authority and RAG source for quality-drift evaluation. |


## Glossary authority

This file is the primary semantic authority for `ados-quality-drift-auditor`.

The evaluator should retrieve relevant concepts from this file before scoring or diagnosing a Project. JSON banks and schemas use term IDs from this glossary and must not silently change their meaning.

## Concept inclusion rule

A concept belongs in this glossary when it helps the auditor understand:

- the User Request, Intent, Goal, Objectives, Project, Package, Archetype, Domain, ADOS Profile, Flow, or Skill;
- ADOS concepts likely to appear in Build Packages, Building Agent Work, or Build Results;
- Goal-Attractor Geometry, Coordinates, Metrics, Pillars, or drift diagnosis;
- ADOS artifact meaning, evidence meaning, or architecture authority.

Generic bookkeeping concepts are excluded unless ADOS gives them a Project-specific boundary.

## Concept map

```text
User Request
→ Intent
   ├── Goal
   │   ├── Objectives
   │   └── Goal-Attractor Geometry
   │       ├── Semantic Meaning Space
   │       ├── Goal Figure / Goal Surface / Goal Attractor
   │       ├── Coordinate Dimensions and Coordinates
   │       └── Metrics
   ├── Project
   │   ├── Archetype
   │   ├── Domain
   │   ├── ADOS Profile and applicable Pillars
   │   ├── Flow and Skill
   │   └── Package versions
   │       ├── Build Package
   │       ├── Building Agent Work
   │       └── Build Result
   └── Quality Drift
       ├── Drift Consequence
       ├── Drift Risk
       ├── Problem Pattern
       └── Corrective Prompt
```

## Interpretation boundary

The glossary defines ADOS execution concepts such as Requirement, Atomic Work, Apply Directive, Verify Directive, Evidence Ledger, and Execution Trace because evaluated Projects may use them.

Their definition here does **not** require every evaluated Project or this auditor to implement those surfaces.


## Semantic spine

### TERM-USER-REQUEST — User Request

**Preferred term:** User Request  
**Russian:** запрос пользователя  
**Status:** approved  
**Concept class:** ADOS intake concept  
**Genus:** user-originated intake artifact  
**Differentia:** contains the raw instruction plus supplied attachments, corrections, constraints, approvals, and context for the current evaluation or build pass

**Definition:** A User Request is the user-originated instruction surface entering ADOS work.

**Scope note:** Use before normalization. Preserve explicit constraints and corrections instead of replacing them with evaluator assumptions.

**Must not mean:**
- Intent
- approved solution
- Requirement
- hidden user preference

**Cardinality / use rule:** One User Request may contain one or more Intents.

**Related terms:** Intent, Goal, Project

**Auditor use:** Establish the earliest traceable source against which later Goal, Objective, and Result alignment can be judged.

**Drift checks:**
- Did the Build Package preserve explicit constraints?
- Did the agent silently omit or reinterpret part of the request?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-INTENT — Intent

**Preferred term:** Intent  
**Russian:** интент / нормализованное намерение  
**Status:** approved  
**Concept class:** ADOS routing concept  
**Genus:** normalized independently routable interpretation  
**Differentia:** preserves one coherent purpose from a User Request and is classified by one primary Archetype and one primary Domain

**Definition:** An Intent is a normalized, independently routable interpretation of a User Request or part of it.

**Scope note:** Use as the routing unit. Split materially different purposes into separate Intents.

**Must not mean:**
- raw User Request
- Requirement
- implementation plan
- inferred hidden wish

**Cardinality / use rule:** One Intent has one primary Archetype and one primary Domain.

**Related terms:** User Request, Archetype, Domain, Goal

**Auditor use:** Detect whether the Build Package or agent routed the work toward a different problem.

**Drift checks:**
- Is the selected Archetype appropriate for the Intent?
- Did the resulting Project solve the intended problem?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-GOAL — Goal

**Preferred term:** Goal  
**Russian:** цель  
**Status:** approved  
**Concept class:** ADOS governance concept  
**Genus:** durable target end state  
**Differentia:** governs a Project, Package, or evaluated scope and anchors Objectives, quality coordinates, and acceptance meaning

**Definition:** A Goal is the durable target end state that governs a Project, Package, or evaluated work scope.

**Scope note:** Use for stable desired meaning and end state, not for route or task detail.

**Must not mean:**
- task list
- feature list
- temporary preference
- single test case

**Cardinality / use rule:** An evaluation should identify one primary Goal; multiple independent Goals require separate Intents or explicit decomposition.

**Related terms:** Intent, Objective, Goal Figure, Quality Drift

**Auditor use:** Serve as the primary attractor against which evolution is evaluated.

**Drift checks:**
- Did later versions preserve the Goal?
- Did local optimizations redefine the desired end state?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-OBJECTIVE — Objective

**Preferred term:** Objective  
**Russian:** задача / целевое направление  
**Status:** approved  
**Concept class:** ADOS governance concept  
**Genus:** material or operational demand vector  
**Differentia:** moves the current Project state toward the Goal by shaping the target region or the route to it without replacing the Goal

**Definition:** An Objective is a material or operational demand that moves work toward the Goal.

**Scope note:** Objectives may be forming, speeding, or forming-and-speeding when Goal-Attractor Geometry is used.

**Must not mean:**
- Requirement
- task
- Atomic Work
- uncontrolled scope addition

**Cardinality / use rule:** A Goal normally has one or more Objectives; each Objective should connect to at least one quality coordinate or delivery expectation.

**Related terms:** Goal, Requirement, Coordinate Dimension, Metric

**Auditor use:** Translate the Goal into concrete audit dimensions and reveal partial or distorted delivery.

**Drift checks:**
- Which Objectives were preserved, weakened, added, or omitted?
- Did a speeding Objective accidentally change the Goal Surface?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-PROJECT — Project

**Preferred term:** Project  
**Russian:** проект  
**Status:** approved  
**Concept class:** ADOS project concept  
**Genus:** top-level governed work container  
**Differentia:** owns the User Request, Intent, Goal, Objectives, Archetype, Domain, Profile expectations, versions, and material deliveries being evaluated

**Definition:** A Project is the top-level governed work container whose quality can evolve across versions.

**Scope note:** Use Project for the full evolving system, not only its repository or final ZIP.

**Must not mean:**
- Package
- repository only
- App only
- single task

**Cardinality / use rule:** One Project may contain many Packages, versions, skills, documents, experiments, or application surfaces.

**Related terms:** Package, Archetype, Domain, Goal, Project Requirement

**Auditor use:** Define the evaluated object and preserve continuity across versions.

**Drift checks:**
- Are compared versions genuinely versions of the same Project?
- Did the Project identity or purpose change without acknowledgment?

**Source/adaptation note:** Generalized from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-PACKAGE — Package

**Preferred term:** Package  
**Russian:** пакет  
**Status:** approved  
**Concept class:** ADOS artifact concept  
**Genus:** versioned artifact envelope  
**Differentia:** materializes a Project or part of it as a governed bundle of documents, data, schemas, instructions, software, or other files

**Definition:** A Package is a materialized, versioned artifact envelope produced or supplied by a Project.

**Scope note:** A Package may be a ZIP, folder, release, or other bounded artifact. It is not the entire Project meaning.

**Must not mean:**
- Project
- loose unbounded file collection
- accepted release by definition

**Cardinality / use rule:** A Project may have zero or more Packages; a Package belongs to one declared Project and version context.

**Related terms:** Project, Build Package, Build Result, PACKAGE.json

**Auditor use:** Provide the material surface for version comparison.

**Drift checks:**
- Does package identity match Project identity?
- Did structure grow while semantic quality declined?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3; artifact-envelope boundary clarified using ADOS Profile v1.23.

### TERM-ARCHETYPE — Archetype

**Preferred term:** Archetype  
**Russian:** архетип / тип проекта  
**Status:** approved  
**Concept class:** ADOS classification concept  
**Genus:** reusable project-shape classifier  
**Differentia:** defines expected delivery form, priority quality coordinates, characteristic risks, and evaluation questions independently of subject Domain

**Definition:** An Archetype classifies what kind of Project or primary Delivery is being evaluated.

**Scope note:** Select one primary Archetype for an evaluation; use Domain separately for subject matter.

**Must not mean:**
- Domain
- runtime instance
- arbitrary tag
- feature type

**Cardinality / use rule:** One Intent and one evaluation use one primary Archetype; secondary characteristics may be noted without changing the primary profile.

**Related terms:** Intent, Domain, Archetype Profile, Metric

**Auditor use:** Select relevant quality coordinates, metrics, and Problem Patterns.

**Drift checks:**
- Was the correct Archetype selected?
- Did a later version drift into a different delivery type?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-ADOS-PROFILE — ADOS Profile

**Preferred term:** ADOS Profile  
**Russian:** профиль ADOS  
**Status:** approved  
**Concept class:** ADOS governance concept  
**Genus:** governing concept and structure profile  
**Differentia:** defines selected ADOS meanings, structural expectations, pillar applicability, and semantic boundaries claimed by a Project or Package

**Definition:** An ADOS Profile is the selected set of ADOS concepts and expectations that a Project or Package claims to follow.

**Scope note:** Use as an evaluation reference, not as proof of compliance merely because a package names the profile.

**Must not mean:**
- generic checklist
- Archetype
- Domain
- self-certified compliance

**Cardinality / use rule:** A Project may reference one primary ADOS Profile and optional compatibility profiles.

**Related terms:** Glossary, Pillar, Archetype, Quality Drift

**Auditor use:** Detect drift from claimed ADOS concept meaning and package principles.

**Drift checks:**
- Which profile concepts are applicable?
- Does the Build Result materially follow them?

**Source/adaptation note:** Adapted from ADOS Profile v1.23; simplified for audit use.

### TERM-DOMAIN — Domain

**Preferred term:** Domain  
**Russian:** предметная область  
**Status:** approved  
**Concept class:** ADOS classification concept  
**Genus:** subject area of governed work  
**Differentia:** defines subject ontology, constraints, metrics, evidence expectations, failure modes, and measurement realities inside an Archetype

**Definition:** A Domain is the subject area in which a Project operates.

**Scope note:** Use Domain to answer what world the Project is about; use Archetype to answer what kind of Project it is.

**Must not mean:**
- Archetype
- workflow class
- package type
- prompt type

**Cardinality / use rule:** One Intent has one primary Domain; related domains may be recorded as secondary context.

**Related terms:** Intent, Archetype, Domain Profile, Metric

**Auditor use:** Apply domain-appropriate quality criteria and risk interpretation.

**Drift checks:**
- Were domain constraints ignored?
- Did evidence quality meet domain expectations?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-FLOW — Flow

**Preferred term:** Flow  
**Russian:** поток  
**Status:** approved  
**Concept class:** ADOS relationship concept  
**Genus:** ordered semantic transformation  
**Differentia:** connects Project concepts or evaluation surfaces in a meaningful order without necessarily prescribing execution mechanics

**Definition:** A Flow is an ordered semantic transformation from one governed state or concept surface to another.

**Scope note:** In this auditor, Flow is an evaluation lens used to locate drift. It is not a mandatory workflow imposed on the agent.

**Must not mean:**
- mandatory execution workflow
- hidden chain of thought
- Execution Trace

**Cardinality / use rule:** A Project may have several Flows; an evaluation should state which Flow it is tracing.

**Related terms:** User Request, Intent, Build Package, Building Agent Work, Build Result

**Auditor use:** Locate where meaning or quality changed between stages.

**Drift checks:**
- At which transition did drift first become visible?
- Was a missing stage incorrectly inferred?

**Source/adaptation note:** Adapted from ADOS workflow doctrine with the non-governance boundary made explicit.

### TERM-SKILL — Skill

**Preferred term:** Skill  
**Russian:** навык / skill  
**Status:** approved  
**Concept class:** ADOS capability concept  
**Genus:** reusable bounded capability or instruction surface  
**Differentia:** declares a purpose, inputs, outputs, interpretation rules, and limits for an agent capability

**Definition:** A Skill is a reusable bounded capability or instruction surface for an agent.

**Scope note:** A Skill may guide evaluation or work but does not imply that its instructions were executed correctly.

**Must not mean:**
- informal ability
- hidden behavior
- arbitrary prompt fragment

**Cardinality / use rule:** One Package may contain multiple Skills; each Skill has one declared primary purpose.

**Related terms:** Prompt, Flow, Building Agent Work, PACKAGE.json

**Auditor use:** Evaluate whether the Skill remains aligned with its Goal and conceptual authority across versions.

**Drift checks:**
- Did the Skill expand beyond its declared purpose?
- Do outputs still match the Skill's Goal?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-GLOSSARY — Glossary

**Preferred term:** Glossary  
**Russian:** глоссарий  
**Status:** approved  
**Concept class:** ADOS semantic-authority concept  
**Genus:** controlled concept and term authority  
**Differentia:** defines approved terms, boundaries, relations, cardinalities, and drift guards for one Project or Profile

**Definition:** A Glossary is the controlled semantic authority used to retrieve and interpret Project concepts consistently.

**Scope note:** In this package, `GLOSSARY.md` is the primary RAG source. Other files reference its term IDs and must not redefine them.

**Must not mean:**
- unordered word list
- documentation index
- generic dictionary

**Cardinality / use rule:** One Package should have one primary Glossary authority for a given semantic scope.

**Related terms:** GLOSSARY.md, Ontology, Taxonomy, Statement

**Auditor use:** Prevent terminology drift and guide concept retrieval before evaluation.

**Drift checks:**
- Do banks use glossary terms consistently?
- Did a version redefine a stable concept locally?

**Source/adaptation note:** Derived from the concept-oriented glossary method in ADOS Glossary v1.3.

## Project evolution and auditor concepts

### TERM-BUILD-PACKAGE — Build Package

**Preferred term:** Build Package  
**Russian:** пакет сборки  
**Status:** approved  
**Concept class:** auditor input concept  
**Genus:** version-specific build-control input set  
**Differentia:** contains prompts and supplied materials that authorize, constrain, or shape a build

**Definition:** A Build Package is the set of prompts, plans, profiles, schemas, examples, baselines, and supplied materials used to shape a build.

**Scope note:** Evaluate what it requires and preserves; do not assume that the building agent followed it.

**Must not mean:**
- Build Result
- Package in general
- agent activity

**Cardinality / use rule:** A version may have zero, one, or several Build Package artifacts; the report should normalize them into one evaluated input surface.

**Related terms:** Prompt, Directive, PDD, Building Agent Work

**Auditor use:** Assess whether the planned change preserves User Request, Goal, Objectives, Archetype, Domain, and ADOS Profile.

**Drift checks:**
- Were acceptance expectations clear?
- Did the Build Package introduce scope or concept drift?

**Source/adaptation note:** Project-specific concept created for this auditor.

### TERM-BUILDING-AGENT-WORK — Building Agent Work

**Preferred term:** Building Agent Work  
**Russian:** работа агента-сборщика  
**Status:** approved  
**Concept class:** auditor input concept  
**Genus:** visible execution and decision surface  
**Differentia:** contains the available response, commands, changes, reasoning summaries, tests, reports, and claims produced while creating a Build Result

**Definition:** Building Agent Work is the visible work performed or claimed by an agent while transforming a Build Package into a Build Result.

**Scope note:** Evaluate only available evidence. Hidden chain-of-thought is neither required nor assumed.

**Must not mean:**
- Build Package
- Build Result
- agent identity
- hidden reasoning

**Cardinality / use rule:** One build may have several work artifacts normalized into one stage evaluation.

**Related terms:** Build Package, Build Result, Execution Trace, QA Evidence

**Auditor use:** Locate control-to-execution drift and unsupported claims.

**Drift checks:**
- Did the agent follow the intended Goal and Objectives?
- Were important decisions or deviations visible?

**Source/adaptation note:** Project-specific concept created for this auditor.

### TERM-BUILD-RESULT — Build Result

**Preferred term:** Build Result  
**Russian:** результат сборки  
**Status:** approved  
**Concept class:** auditor input concept  
**Genus:** produced version or artifact  
**Differentia:** is the Project version, Package, file set, deployment, or other material output resulting from building-agent work

**Definition:** A Build Result is the produced Project version or material artifact after a build.

**Scope note:** A Build Result may be incomplete or failed; result does not imply acceptance.

**Must not mean:**
- Build Package
- Building Agent Work
- validated release by definition

**Cardinality / use rule:** One evaluated build has one normalized Build Result, which may contain several artifacts.

**Related terms:** Package, Delivery, Baseline Version, Quality Drift

**Auditor use:** Assess delivered quality and compare it with the intended and baseline states.

**Drift checks:**
- What was actually delivered?
- Which expected meanings or properties changed?

**Source/adaptation note:** Project-specific concept created for this auditor.

### TERM-BASELINE-VERSION — Baseline Version

**Preferred term:** Baseline Version  
**Russian:** базовая версия  
**Status:** approved  
**Concept class:** auditor comparison concept  
**Genus:** quality reference version  
**Differentia:** is selected because it offers the strongest verified reference for the intended comparison, not merely because it is latest

**Definition:** A Baseline Version is the Project version used as the reference for preservation, regression, and drift analysis.

**Scope note:** Baseline selection should state the relevant Goal, confidence, and why alternatives were not selected.

**Must not mean:**
- latest version by default
- perfect version
- Donor Component

**Cardinality / use rule:** One comparison uses one primary Baseline Version.

**Related terms:** Build Result, Quality Drift, Metric, Project

**Auditor use:** Prevent recency bias and expose regressions hidden by structural growth.

**Drift checks:**
- Was the baseline selected by evidence?
- Would an older version provide a stronger contract reference?

**Source/adaptation note:** Project-specific concept created for this auditor from prior ADOS evaluation findings.

### TERM-QUALITY-DRIFT — Quality Drift

**Preferred term:** Quality Drift  
**Russian:** дрейф качества  
**Status:** approved  
**Concept class:** auditor core concept  
**Genus:** quality-relevant divergence  
**Differentia:** moves a Project, Package, stage, or version away from its User Request, Intent, Goal, Objectives, Archetype, Domain, ADOS Profile, or verified Baseline expectation

**Definition:** Quality Drift is a quality-relevant divergence from the governing semantic or quality frame.

**Scope note:** Not every change is drift. Intentional, authorized, verified change may be improvement.

**Must not mean:**
- any difference
- new feature
- numeric score delta alone

**Cardinality / use rule:** A drift finding identifies at least one source frame, affected coordinate, direction, and consequence or uncertainty.

**Related terms:** Goal, Objective, Coordinate Dimension, Drift Consequence

**Auditor use:** Central object of the auditor.

**Drift checks:**
- What changed?
- Against which governing concept?
- Why does the difference matter?

**Source/adaptation note:** Project-specific concept created for this auditor.

### TERM-DRIFT-CONSEQUENCE — Drift Consequence

**Preferred term:** Drift Consequence  
**Russian:** последствие дрейфа  
**Status:** approved  
**Concept class:** auditor impact concept  
**Genus:** observed effect of Quality Drift  
**Differentia:** describes the demonstrated effect on meaning, correctness, utility, maintainability, compliance, or future work

**Definition:** A Drift Consequence is an observed effect caused by Quality Drift.

**Scope note:** Separate observed consequence from future risk.

**Must not mean:**
- possible future harm
- drift signal
- root cause

**Cardinality / use rule:** One drift may have zero or more confirmed consequences.

**Related terms:** Quality Drift, Drift Risk, Problem Pattern

**Auditor use:** Explain why a finding affects Project quality.

**Drift checks:**
- Is the consequence directly observed?
- Which delivery or coordinate was affected?

**Source/adaptation note:** Project-specific concept created for this auditor.

### TERM-DRIFT-RISK — Drift Risk

**Preferred term:** Drift Risk  
**Russian:** риск дрейфа  
**Status:** approved  
**Concept class:** auditor risk concept  
**Genus:** credible future failure mode  
**Differentia:** may occur if detected Quality Drift remains unresolved

**Definition:** A Drift Risk is a credible future failure mode caused by unresolved Quality Drift.

**Scope note:** State likelihood or confidence separately from severity when possible.

**Must not mean:**
- confirmed consequence
- generic concern
- unsupported speculation

**Cardinality / use rule:** One drift may have zero or more Drift Risks.

**Related terms:** Quality Drift, Drift Consequence, Corrective Prompt

**Auditor use:** Prioritize corrective action without presenting inference as fact.

**Drift checks:**
- What evidence supports the risk?
- What control or correction would reduce it?

**Source/adaptation note:** Project-specific concept created for this auditor.

### TERM-PROBLEM-PATTERN — Problem Pattern

**Preferred term:** Problem Pattern  
**Russian:** шаблон проблемы  
**Status:** approved  
**Concept class:** auditor diagnostic concept  
**Genus:** reusable diagnosis model  
**Differentia:** connects observable signals, affected concepts, typical causes, visible effects, consequences, risks, confirmation methods, and repairs

**Definition:** A Problem Pattern is a reusable model for diagnosing recurring quality or drift failures.

**Scope note:** Match only when applicable signals are present. A keyword alone is not sufficient.

**Must not mean:**
- glossary term
- automatic verdict
- universal root cause

**Cardinality / use rule:** One finding may match several Problem Patterns; one primary pattern should be identified when possible.

**Related terms:** Quality Drift, Drift Risk, Corrective Prompt

**Auditor use:** Convert repeated failure modes into consistent diagnosis and repair guidance.

**Drift checks:**
- Which signals are observed?
- Could an exclusion make the pattern inapplicable?

**Source/adaptation note:** Project-specific concept created for this auditor.

### TERM-CORRECTIVE-PROMPT — Corrective Prompt

**Preferred term:** Corrective Prompt  
**Russian:** корректирующий промпт  
**Status:** approved  
**Concept class:** auditor output concept  
**Genus:** focused repair instruction  
**Differentia:** targets observed drift or a Problem Pattern while preserving the governing Goal and minimizing unrelated scope

**Definition:** A Corrective Prompt is a focused instruction fragment for repairing a specific quality defect or drift mechanism.

**Scope note:** It should name the problem, affected surfaces, required result, and drift protections.

**Must not mean:**
- complete rebuild prompt by default
- generic improve-quality request
- unscoped rewrite

**Cardinality / use rule:** A report may contain one combined Corrective Prompt or several ordered fragments.

**Related terms:** Problem Pattern, Goal, Objective, Build Package

**Auditor use:** Translate diagnosis into next-version action.

**Drift checks:**
- Does the prompt repair the cause rather than the symptom?
- Does it avoid changing unrelated concepts?

**Source/adaptation note:** Project-specific concept created for this auditor.

## ADOS prompt, work, and requirement concepts

### TERM-PROMPT — Prompt

**Preferred term:** Prompt  
**Russian:** промпт  
**Status:** approved  
**Concept class:** ADOS instruction concept  
**Genus:** model-facing instruction artifact  
**Differentia:** provides context, requested behavior, constraints, examples, or output expectations to an agent or model

**Definition:** A Prompt is a model-facing instruction artifact.

**Scope note:** Use Prompt for a bounded instruction surface that may include several directives or contextual elements.

**Must not mean:**
- Skill by definition
- hidden reasoning
- Work
- Requirement

**Cardinality / use rule:** A Build Package may contain many Prompts.

**Related terms:** Directive, Prompt Archetype, Build Package

**Auditor use:** Evaluate instruction clarity, Goal alignment, and scope effects.

**Drift checks:**
- Did the Prompt preserve the Intent?
- Did examples or wording bias the agent toward the wrong result?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-DIRECTIVE — Directive

**Preferred term:** Directive  
**Russian:** директива  
**Status:** approved  
**Concept class:** ADOS instruction concept  
**Genus:** minimal bounded Prompt subtype  
**Differentia:** issues one scoped command or verification request without representing the work object itself

**Definition:** A Directive is a minimal bounded subtype of Prompt.

**Scope note:** ADOS commonly distinguishes Apply Directive and Verify Directive. The auditor may inspect such directives when present.

**Must not mean:**
- Work
- Atomic Work
- Requirement
- Evidence
- general prose

**Cardinality / use rule:** A Directive should have one primary action or verification purpose.

**Related terms:** Prompt, Apply Directive, Verify Directive

**Auditor use:** Distinguish instruction quality from work/result quality.

**Drift checks:**
- Does the Directive alter or verify the intended target?
- Was a directive mistaken for proof of execution?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-DELIVERY — Delivery

**Preferred term:** Delivery  
**Russian:** поставка / поставление  
**Status:** approved  
**Concept class:** ADOS output concept  
**Genus:** governed production of material output  
**Differentia:** produces a document, file set, Package, report, software artifact, or other accepted output surface

**Definition:** Delivery is the act or outcome surface by which a Project produces material output.

**Scope note:** A Build Result may be a Delivery even when its quality is poor; acceptance is a separate judgment.

**Must not mean:**
- upload alone
- Project itself
- quality acceptance by definition

**Cardinality / use rule:** A Project may have one or more Deliveries per version.

**Related terms:** Project, Package, Build Result, QA Evidence

**Auditor use:** Identify what the Project materially produced.

**Drift checks:**
- Did the Delivery match the intended artifact type?
- Were key deliverables missing or substituted?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-WORK — Work

**Preferred term:** Work  
**Russian:** работа  
**Status:** approved  
**Concept class:** ADOS planning concept  
**Genus:** non-specific execution or activity grouping  
**Differentia:** describes effort or action that may not be decomposed to a specific Atomic Work

**Definition:** Work is an abstract grouping of execution or activity.

**Scope note:** The auditor may discuss Work without requiring it to be file-grounded or represented in a Work Plan.

**Must not mean:**
- Atomic Work
- Requirement
- evidence
- result

**Cardinality / use rule:** Work may aggregate zero or more Atomic Works or other actions.

**Related terms:** Atomic Work, Building Agent Work, Directive

**Auditor use:** Describe visible agent activity without imposing ADOS execution cardinality.

**Drift checks:**
- Is the Work sufficiently visible to evaluate?
- Did abstract Work conceal material scope changes?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 with the auditor non-governance boundary.

### TERM-APPLY-DIRECTIVE — Apply Directive

**Preferred term:** Apply Directive  
**Russian:** директива применения  
**Status:** approved  
**Concept class:** ADOS instruction concept  
**Genus:** Directive that requests mutation  
**Differentia:** asks an agent to create, modify, delete, configure, or otherwise change a declared target

**Definition:** An Apply Directive is a Directive that requests a change to a target artifact or state.

**Scope note:** In strict ADOS execution models it may belong to one Atomic Work; this auditor does not impose that model.

**Must not mean:**
- Verify Directive
- proof of completion
- Work itself

**Cardinality / use rule:** One Apply Directive should state one primary mutation purpose.

**Related terms:** Directive, Atomic Work, Verify Directive

**Auditor use:** Evaluate whether requested changes were clear, authorized, and aligned.

**Drift checks:**
- Did the Apply Directive exceed scope?
- Did the result reflect the requested mutation?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-VERIFY-DIRECTIVE — Verify Directive

**Preferred term:** Verify Directive  
**Russian:** директива проверки  
**Status:** approved  
**Concept class:** ADOS instruction concept  
**Genus:** Directive that requests verification  
**Differentia:** checks a target or result against stated criteria and may produce QA Evidence

**Definition:** A Verify Directive is a Directive that requests verification of an applied change or target state.

**Scope note:** Verification can be file-level, semantic, functional, or other bounded check. It is not delivery acceptance by itself.

**Must not mean:**
- Apply Directive
- QA Evidence itself
- package release verdict

**Cardinality / use rule:** One Verify Directive should identify its target and criteria.

**Related terms:** Directive, Apply Directive, QA Evidence, Atomic Work

**Auditor use:** Assess whether the check actually tests the intended property.

**Drift checks:**
- Was the criterion explicit?
- Could the check pass for the wrong reason?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-PDD — PDD

**Preferred term:** PDD  
**Russian:** PDD / документ определения проекта  
**Status:** approved  
**Concept class:** ADOS project-definition concept  
**Genus:** Project Definition Document or governed document set  
**Differentia:** turns accepted Intent, Goal, Objectives, Requirements, architecture, delivery expectations, and verification meaning into a coherent Project definition

**Definition:** A PDD is a Project Definition Document or governed document set that defines a Project and its intended Delivery.

**Scope note:** PDD may be present in evaluated Projects. This auditor does not require every Project to use one.

**Must not mean:**
- raw User Request
- Work Plan
- final Package
- passive prose only

**Cardinality / use rule:** A PDD has one primary definition surface and may reference supporting documents.

**Related terms:** Project, Goal, Objective, Project Requirement, Build Package

**Auditor use:** Evaluate whether the Build Package has a coherent project definition and whether later stages preserve it.

**Drift checks:**
- Does the PDD reflect the User Request?
- Did the agent or result silently redefine the PDD?

**Source/adaptation note:** Definition adapted from ADOS Glossary v1.3; app-specific assumptions removed.

### TERM-STATEMENT — Statement

**Preferred term:** Statement  
**Russian:** смысловое высказывание  
**Status:** approved  
**Concept class:** ADOS semantic-unit concept  
**Genus:** discrete meaning-bearing text unit  
**Differentia:** expresses a proposition, rule, fact, definition, rationale, classification, obligation, or command-like content

**Definition:** A Statement is a discrete semantic unit in a document or structured record.

**Scope note:** Use as the neutral unit before classifying the content as Claim, Requirement, definition, or instruction.

**Must not mean:**
- Claim by default
- Requirement by default
- Evidence
- Work

**Cardinality / use rule:** One Statement may contain one or more Atomic Claims; good authoring prefers separable meanings.

**Related terms:** Claim, Atomic Claim, Glossary, Prompt

**Auditor use:** Support semantic comparison and detect bundled or changed meaning.

**Drift checks:**
- Did one Statement combine independent claims?
- Did wording change normative force?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-CLAIM — Claim

**Preferred term:** Claim  
**Russian:** проверяемое утверждение  
**Status:** approved  
**Concept class:** ADOS assertion concept  
**Genus:** evidence-requiring Statement  
**Differentia:** asserts a checkable fact, state, property, compliance result, quality, performance, or evaluation outcome

**Definition:** A Claim is a Statement that can be supported, contradicted, qualified, or left unconfirmed by source or evidence.

**Scope note:** Obligations are Requirements, not Claims. Evidence is not the Claim it supports.

**Must not mean:**
- Requirement
- Evidence
- Objective
- proof by itself

**Cardinality / use rule:** A Claim may decompose into one or more Atomic Claims.

**Related terms:** Statement, Atomic Claim, QA Evidence, Evidence Ledger

**Auditor use:** Separate what a source asserts from what the auditor can confirm.

**Drift checks:**
- What evidence supports this Claim?
- Is the Claim broader than the evidence?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-ATOMIC-CLAIM — Atomic Claim

**Preferred term:** Atomic Claim  
**Russian:** атомарное проверяемое утверждение  
**Status:** approved  
**Concept class:** ADOS assertion concept  
**Genus:** smallest independently assessable Claim  
**Differentia:** contains one independently supportable or refutable assertion

**Definition:** An Atomic Claim is the smallest independently assessable Claim.

**Scope note:** Use for evaluation when a compound Claim would hide mixed support or contradiction.

**Must not mean:**
- Requirement
- Work unit
- Goal
- Evidence

**Cardinality / use rule:** One Atomic Claim expresses one independently assessable proposition.

**Related terms:** Claim, Statement, QA Evidence

**Auditor use:** Enable precise comparison and evidence scoping without requiring a claim ledger.

**Drift checks:**
- Can this assertion be assessed independently?
- Does its evidence support the entire assertion?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-REQUIREMENT — Requirement

**Preferred term:** Requirement  
**Russian:** требование  
**Status:** approved  
**Concept class:** ADOS obligation concept  
**Genus:** accepted implementable and verifiable obligation  
**Differentia:** constrains Project or Delivery behavior, content, structure, or quality and can be evaluated against evidence

**Definition:** A Requirement is an accepted obligation that is implementable, assessable, and linked to the Project's Goal or Objectives.

**Scope note:** Requirements may come from a PDD, profile, contract, regulation, or explicit User Request.

**Must not mean:**
- Claim
- Objective
- task
- unapproved wish

**Cardinality / use rule:** One Requirement may decompose into one or more Atomic Requirements.

**Related terms:** Objective, Project Requirement, Atomic Requirement, PDD

**Auditor use:** Assess obligation coverage and identify requirement drift.

**Drift checks:**
- Was the Requirement applicable?
- Was it changed, omitted, or satisfied only superficially?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-PROJECT-REQUIREMENT — Project Requirement

**Preferred term:** Project Requirement  
**Russian:** требование проекта  
**Status:** approved  
**Concept class:** ADOS obligation concept  
**Genus:** Requirement owned by a specific Project  
**Differentia:** expresses a Project-specific obligation independently of whether the Archetype is app, research, runtime, profile, prompt, or other

**Definition:** A Project Requirement is a Requirement owned by the evaluated Project.

**Scope note:** Use this general term instead of `App Requirement` unless the obligation is genuinely specific to the App Archetype.

**Must not mean:**
- Governance Requirement
- Objective
- App Requirement as universal term

**Cardinality / use rule:** Each Project Requirement belongs to one Project and may reference one or more Goals, Objectives, concepts, or deliveries.

**Related terms:** Project, Requirement, Atomic Requirement, Archetype

**Auditor use:** Generalize source methodology across all supported Archetypes.

**Drift checks:**
- Was an app-specific rule incorrectly applied to a non-app Project?
- Does the Requirement remain relevant to the selected Archetype?

**Source/adaptation note:** Adapted from ADOS Profile v1.23 by replacing app-specific ownership with Project ownership.

### TERM-ATOMIC-REQUIREMENT — Atomic Requirement

**Preferred term:** Atomic Requirement  
**Russian:** атомарное требование  
**Status:** approved  
**Concept class:** ADOS obligation concept  
**Genus:** indivisible verifiable Requirement  
**Differentia:** expresses one obligation that can be independently assessed without splitting normative force

**Definition:** An Atomic Requirement is the smallest independently verifiable obligation derived from one Requirement.

**Scope note:** Evaluated Projects may use Atomic Requirements; the auditor does not require them.

**Must not mean:**
- Atomic Claim
- Atomic Work
- test case
- Goal

**Cardinality / use rule:** One Atomic Requirement derives from one parent Requirement.

**Related terms:** Requirement, Project Requirement, Atomic Work

**Auditor use:** Assess whether decomposition preserved obligation meaning.

**Drift checks:**
- Was an obligation bundled or fragmented incorrectly?
- Did the agent satisfy only part of it?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-ATOMIC-WORK — Atomic Work

**Preferred term:** Atomic Work  
**Russian:** атомарная работа  
**Status:** approved  
**Concept class:** ADOS execution concept  
**Genus:** bounded executable work unit  
**Differentia:** is derived from one Atomic Requirement and has a clearly declared target and verification meaning in ADOS models that use it

**Definition:** Atomic Work is a bounded executable work unit used by some ADOS Projects.

**Scope note:** The strict v1.3 model targets one File with one Apply and Verify pair. This auditor defines that model for interpretation but does not impose it.

**Must not mean:**
- Atomic Requirement
- Claim
- Evidence
- mandatory unit for every Project

**Cardinality / use rule:** Where the strict ADOS file-grounded model applies, one Atomic Work targets one File; otherwise applicability must be stated.

**Related terms:** Atomic Requirement, Apply Directive, Verify Directive, Work

**Auditor use:** Audit work decomposition when the evaluated Project claims ADOS Atomic Work compliance.

**Drift checks:**
- Does the Work match the claimed ADOS model?
- Was multi-target work mislabeled as Atomic?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3; applicability boundary added.

## Goal-Attractor Geometry and measurement

### TERM-SEMANTIC-MEANING-SPACE — Semantic Meaning Space

**Preferred term:** Semantic Meaning Space  
**Russian:** семантическое пространство значений  
**Status:** approved  
**Concept class:** ADOS geometry concept  
**Genus:** virtual multidimensional interpretation space  
**Differentia:** locates current Project state, desired end state, boundaries, and evaluation coordinates under an Archetype and Domain

**Definition:** Semantic Meaning Space is the conceptual multidimensional space in which Project quality coordinates are interpreted.

**Scope note:** It is a governance and evaluation model, not a claim of literal physical space.

**Must not mean:**
- embedding vector by default
- physical geometry
- single score

**Cardinality / use rule:** One evaluation defines one primary Semantic Meaning Space from the selected Archetype, Domain, Goal, and Profile.

**Related terms:** Goal-Attractor Geometry, Coordinate Dimension, Goal Figure

**Auditor use:** Provide a coherent frame for multi-dimensional drift analysis.

**Drift checks:**
- Are coordinates interpreted under the correct Archetype and Domain?
- Did the frame change between versions?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-GOAL-ATTRACTOR-GEOMETRY — Goal-Attractor Geometry

**Preferred term:** Goal-Attractor Geometry  
**Russian:** геометрия Goal-Attractor  
**Status:** approved  
**Concept class:** ADOS geometry concept  
**Genus:** project-governance geometry model  
**Differentia:** represents current state, Goal Figure, Goal Surface, Coordinate Dimensions, Metrics, and movement toward or away from the Goal

**Definition:** Goal-Attractor Geometry is an operational semantic model for evaluating Project movement relative to its Goal and Objectives.

**Scope note:** Use diagnostically. Do not overclaim literal mathematical or physical attractor properties unless formally defined.

**Must not mean:**
- single score
- mandatory implementation workflow
- physical dynamics

**Cardinality / use rule:** One evaluation may define one geometry per Intent or Project scope.

**Related terms:** Goal, Goal Figure, Coordinate Dimension, Metric, Quality Drift

**Auditor use:** Represent improvement, degradation, and mixed movement across coordinates.

**Drift checks:**
- Which coordinates moved?
- Did improvement in one dimension conceal degradation in another?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-GOAL-FIGURE — Goal Figure

**Preferred term:** Goal Figure  
**Russian:** целевая фигура  
**Status:** approved  
**Concept class:** ADOS geometry concept  
**Genus:** desired end-state figure  
**Differentia:** combines the Goal center statement, Goal Surface, adjacent-scope boundaries, and material Deliveries

**Definition:** A Goal Figure is the structured desired end state inside Semantic Meaning Space.

**Scope note:** Use to make the Goal assessable without reducing it to one scalar.

**Must not mean:**
- Goal text alone
- single Metric
- implementation plan

**Cardinality / use rule:** One Goal normally defines one Goal Figure for an evaluation scope.

**Related terms:** Goal, Goal Surface, Delivery, Objective

**Auditor use:** Clarify what success looks like across several quality dimensions.

**Drift checks:**
- Is the Goal Figure sufficiently bounded?
- Did a later version change the intended Deliveries?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-GOAL-SURFACE — Goal Surface

**Preferred term:** Goal Surface  
**Russian:** поверхность цели  
**Status:** approved  
**Concept class:** ADOS geometry concept  
**Genus:** boundary of the Goal Figure  
**Differentia:** distinguishes in-scope successful states from adjacent or insufficient states

**Definition:** The Goal Surface is the boundary of the Goal Figure used to judge whether the Project state is within the intended success region.

**Scope note:** The surface may be qualitative, metric-based, or mixed.

**Must not mean:**
- single pass/fail flag
- Goal itself
- test suite

**Cardinality / use rule:** A Goal Figure has one conceptual Goal Surface that may contain several coordinate conditions.

**Related terms:** Goal Figure, Coordinate Dimension, Metric, Attractor Basin

**Auditor use:** Make acceptance meaning explicit without imposing a build process.

**Drift checks:**
- Which coordinate conditions define success?
- Were they weakened or changed?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-GOAL-ATTRACTOR — Goal Attractor

**Preferred term:** Goal Attractor  
**Russian:** аттрактор цели  
**Status:** approved  
**Concept class:** ADOS geometry concept  
**Genus:** dynamic governance pull  
**Differentia:** orients Objectives, evaluation, and corrective action toward the Goal Figure across Coordinate Dimensions

**Definition:** A Goal Attractor is the governance construct representing directional pull toward the Goal Figure.

**Scope note:** It is a semantic and diagnostic construct, not a literal force.

**Must not mean:**
- Goal
- single Metric
- mandatory workflow

**Cardinality / use rule:** One Goal Figure may define one primary Goal Attractor.

**Related terms:** Goal Figure, Objective, Convergence Vector, Quality Drift

**Auditor use:** Interpret whether version changes move toward or away from the intended state.

**Drift checks:**
- Do corrections reduce distance on priority coordinates?
- Did activity increase without convergence?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-ATTRACTOR-BASIN — Attractor Basin

**Preferred term:** Attractor Basin  
**Russian:** бассейн аттрактора  
**Status:** approved  
**Concept class:** ADOS geometry concept  
**Genus:** acceptable implementation region  
**Differentia:** contains legitimate variants that preserve the identity and boundary of the Goal Figure

**Definition:** An Attractor Basin is the region of acceptable implementation variants around the Goal Surface.

**Scope note:** Use to avoid labeling every implementation difference as drift.

**Must not mean:**
- unlimited scope
- all possible solutions
- Goal Surface

**Cardinality / use rule:** One Goal Figure may have one or more described acceptable regions.

**Related terms:** Goal Surface, Quality Drift, Archetype

**Auditor use:** Distinguish legitimate variation from quality degradation.

**Drift checks:**
- Is the new version still inside the acceptable region?
- Did a style change preserve the Goal identity?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-COORDINATE — Coordinate

**Preferred term:** Coordinate  
**Russian:** координата  
**Status:** approved  
**Concept class:** ADOS geometry concept  
**Genus:** located value on one Coordinate Dimension  
**Differentia:** represents the current, target, or compared Project state for one separable semantic concern

**Definition:** A Coordinate is a value or assessed position on a Coordinate Dimension.

**Scope note:** A Coordinate may be numeric, ordinal, categorical, or qualitative when the scale is defined.

**Must not mean:**
- Coordinate Dimension
- Metric
- unexplained score

**Cardinality / use rule:** Each active Coordinate Dimension has at most one normalized current Coordinate per evaluated version and surface.

**Related terms:** Coordinate Dimension, Metric, Build Result, Quality Drift

**Auditor use:** Represent where a stage or version stands on a quality dimension.

**Drift checks:**
- Is the value comparable across versions?
- Is the scale and evidence stated?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-COORDINATE-DIMENSION — Coordinate Dimension

**Preferred term:** Coordinate Dimension  
**Russian:** координатное измерение  
**Status:** approved  
**Concept class:** ADOS geometry concept  
**Genus:** named separable dimension of Semantic Meaning Space  
**Differentia:** represents one Project quality or meaning concern with a defined scale, polarity, target condition, and interpretation

**Definition:** A Coordinate Dimension is a named dimension used to locate and compare Project states.

**Scope note:** Coordinate Dimensions should be conceptually distinct enough to avoid double-counting.

**Must not mean:**
- Pillar
- Metric
- folder category
- arbitrary score label

**Cardinality / use rule:** Each dimension has one stable ID and one interpretation per active geometry.

**Related terms:** Coordinate, Metric, Goal Surface, Pillar

**Auditor use:** Organize evaluation into interpretable quality directions.

**Drift checks:**
- Does the dimension correspond to a Goal or Objective?
- Did its meaning change across versions?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-METRIC — Metric

**Preferred term:** Metric  
**Russian:** метрика  
**Status:** approved  
**Concept class:** ADOS measurement concept  
**Genus:** defined measurement or scoring rule  
**Differentia:** maps evidence or assessed conditions to a value used to interpret one or more Coordinate Dimensions

**Definition:** A Metric is a defined procedure or rubric for measuring a Project quality property.

**Scope note:** Metrics are guardrails for interpretation. They do not replace semantic judgment or establish release acceptance by themselves.

**Must not mean:**
- Coordinate Dimension
- Goal
- test count
- number without scale

**Cardinality / use rule:** A Metric should reference at least one Coordinate Dimension and define scale, polarity, and evidence expectations.

**Related terms:** Coordinate Dimension, Evaluation Metric, Metric Guardrail, QA Evidence

**Auditor use:** Provide consistent comparison without metric substitution.

**Drift checks:**
- Does the Metric measure the intended concept?
- Can it improve while core quality declines?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-EVALUATION-METRIC — Evaluation Metric

**Preferred term:** Evaluation Metric  
**Russian:** оценочная метрика  
**Status:** approved  
**Concept class:** ADOS measurement concept  
**Genus:** Metric used for Project evaluation  
**Differentia:** produces a score or classification from evidence, Coordinate values, rubrics, or defined checks

**Definition:** An Evaluation Metric is a Metric used to assess a Project, stage, version, or drift dimension.

**Scope note:** This auditor normally uses 0–10 scores with separate confidence and evidence status.

**Must not mean:**
- release verdict
- evidence itself
- Coordinate Dimension

**Cardinality / use rule:** Each reported Evaluation Metric belongs to one defined metric record.

**Related terms:** Metric, Metric Guardrail, Coordinate, Report Policy

**Auditor use:** Support repeatable stage and cross-version assessment.

**Drift checks:**
- Is confidence separate from score?
- Is missing evidence represented honestly?

**Source/adaptation note:** Adapted from ADOS Profile v1.23; scale adapted for this auditor.

### TERM-METRIC-GUARDRAIL — Metric Guardrail

**Preferred term:** Metric Guardrail  
**Russian:** метрический ограничитель  
**Status:** approved  
**Concept class:** auditor measurement concept  
**Genus:** interpretive boundary for Metric use  
**Differentia:** prevents scores from replacing Goal, semantic, evidence, or Archetype reasoning

**Definition:** A Metric Guardrail is a rule limiting how an Evaluation Metric may be interpreted.

**Scope note:** Guardrails are report rules, not execution gates.

**Must not mean:**
- hard build gate
- Metric itself
- automatic verdict

**Cardinality / use rule:** Each Metric may cite zero or more Metric Guardrails.

**Related terms:** Metric, Goal, Report Policy, Problem Pattern

**Auditor use:** Prevent false precision and score-driven drift.

**Drift checks:**
- Was a count mistaken for quality?
- Was confidence or evidence status omitted?

**Source/adaptation note:** Project-specific concept created for this auditor.

### TERM-PILLAR — Pillar

**Preferred term:** Pillar  
**Russian:** столп / доктринальный принцип  
**Status:** approved  
**Concept class:** ADOS doctrine concept  
**Genus:** durable cross-cutting ADOS doctrine  
**Differentia:** constrains concept interpretation, requirement selection, evaluation, evidence, or repair across Projects

**Definition:** A Pillar is a durable cross-cutting ADOS doctrine.

**Scope note:** Pillars are static authority concepts. Coordinate Dimensions are dynamic Project quality dimensions.

**Must not mean:**
- Coordinate Dimension
- Requirement
- Metric
- file type

**Cardinality / use rule:** The ADOS Pillar Set contains the approved Pillars; a Project or Archetype profile selects applicable Pillars.

**Related terms:** ADOS Pillar Set, Coordinate Dimension, ADOS Profile

**Auditor use:** Assess whether a Project claiming ADOS alignment preserves applicable doctrine.

**Drift checks:**
- Which Pillars apply?
- Was a Pillar copied without applicability analysis?

**Source/adaptation note:** Adapted from ADOS Profile v1.23.

### TERM-ADOS-PILLAR-SET — ADOS Pillar Set

**Preferred term:** ADOS Pillar Set  
**Russian:** набор столпов ADOS  
**Status:** approved  
**Concept class:** ADOS doctrine concept  
**Genus:** governed collection of Pillars  
**Differentia:** contains the stable pillar IDs and meanings used by an ADOS Profile

**Definition:** The ADOS Pillar Set is the governed collection of ADOS Pillars.

**Scope note:** v0.2 records all v1.23 pillars but does not assume every Pillar is mandatory for every evaluated Project.

**Must not mean:**
- Archetype Profile
- Metric bank
- flat checklist

**Cardinality / use rule:** One ADOS Profile version has one declared Pillar Set.

**Related terms:** Pillar, ADOS Profile, Archetype

**Auditor use:** Provide stable doctrine references without converting them into quality coordinates.

**Drift checks:**
- Did the selected profile identify applicable Pillars?
- Were dynamic coordinates incorrectly treated as static pillars?

**Source/adaptation note:** Pillar list adapted from ADOS Profile v1.23.

## ADOS file, architecture, and evidence concepts

### TERM-PACKAGE-JSON — PACKAGE.json

**Preferred term:** PACKAGE.json  
**Russian:** PACKAGE.json  
**Status:** approved  
**Concept class:** ADOS document concept  
**Genus:** machine package-identity document  
**Differentia:** declares package name, version, Goal, Objectives, semantic authority, entrypoints, methodology sources, and non-goals without duplicating the full Project model

**Definition:** `PACKAGE.json` is the machine-readable package identity and entrypoint record.

**Scope note:** It describes the distributable package, not every Project attribute or report result.

**Must not mean:**
- manifest inventory
- Glossary
- PDD
- human overview

**Cardinality / use rule:** One Package has at most one active root `PACKAGE.json`.

**Related terms:** Package, README.md, MANIFEST.md, Goal

**Auditor use:** Audit package identity, purpose, and entrypoint drift.

**Drift checks:**
- Do version and Goal agree with other active surfaces?
- Does the file duplicate or contradict the Glossary?

**Source/adaptation note:** Content principle adapted from ADOS Profile v1.23 package metadata.

### TERM-MANIFEST-MD — MANIFEST.md

**Preferred term:** MANIFEST.md  
**Russian:** MANIFEST.md  
**Status:** approved  
**Concept class:** ADOS document concept  
**Genus:** agent navigation and authority document  
**Differentia:** declares authority order, package surface roles, and how an agent should load the package without duplicating semantic definitions

**Definition:** `MANIFEST.md` is the agent-facing navigation and authority map for a Package.

**Scope note:** It should describe where authority lives. In this auditor it does not impose a build workflow.

**Must not mean:**
- machine file inventory by default
- README.md
- Glossary
- PDD

**Cardinality / use rule:** One Package should have one active root `MANIFEST.md`.

**Related terms:** PACKAGE.json, README.md, GLOSSARY.md, ADR

**Auditor use:** Audit authority ambiguity and stale path references.

**Drift checks:**
- Does the load order point to current files?
- Does the manifest over-govern execution?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-README-MD — README.md

**Preferred term:** README.md  
**Russian:** README.md  
**Status:** approved  
**Concept class:** ADOS document concept  
**Genus:** human package entrypoint  
**Differentia:** explains purpose, boundaries, usage, and major surfaces to a human without becoming the semantic or architecture authority

**Definition:** `README.md` is the primary human-readable entrypoint for a Package.

**Scope note:** Keep it concise and link to authoritative surfaces.

**Must not mean:**
- Glossary
- PDD
- Manifest
- complete architecture record

**Cardinality / use rule:** One Package should have one active root `README.md`.

**Related terms:** PACKAGE.json, MANIFEST.md, GLOSSARY.md

**Auditor use:** Audit whether human-facing claims agree with machine and semantic authority.

**Drift checks:**
- Does README overclaim capability?
- Does it point to correct active entrypoints?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23.

### TERM-GLOSSARY-MD — GLOSSARY.md

**Preferred term:** GLOSSARY.md  
**Russian:** GLOSSARY.md  
**Status:** approved  
**Concept class:** ADOS document concept  
**Genus:** primary human semantic-authority document  
**Differentia:** materializes the approved Glossary terms, boundaries, relations, and drift guards for one Package

**Definition:** `GLOSSARY.md` is the primary human-readable semantic authority for this auditor.

**Scope note:** Banks, docs, schemas, and reports reference term IDs and should not redefine them.

**Must not mean:**
- README.md
- unordered term list
- problem bank

**Cardinality / use rule:** One Package semantic scope has one active primary `GLOSSARY.md`.

**Related terms:** Glossary, Ontology, Taxonomy, PACKAGE.json

**Auditor use:** Audit terminology and definition drift.

**Drift checks:**
- Are referenced term IDs present?
- Did another file redefine a term?

**Source/adaptation note:** Derived from the concept-oriented glossary methodology of ADOS Glossary v1.3.

### TERM-PDD-MD — PDD.md

**Preferred term:** PDD.md  
**Russian:** PDD.md  
**Status:** approved  
**Concept class:** ADOS document concept  
**Genus:** Project-definition document surface  
**Differentia:** materializes the accepted Project Goal, Objectives, scope, architecture boundaries, and intended Deliveries

**Definition:** `PDD.md` is the primary human Project-definition surface when a Project uses a PDD.

**Scope note:** This auditor includes its own `PDD.md` but does not require one from every evaluated Project.

**Must not mean:**
- MANIFEST.md
- README.md
- Work Plan

**Cardinality / use rule:** A Project using a single-document PDD has one primary `PDD.md`; document-set forms may name another primary file.

**Related terms:** PDD, Goal, Objective, Project Requirement

**Auditor use:** Audit project-definition drift.

**Drift checks:**
- Does the PDD match PACKAGE.json Goal/Objectives?
- Did later versions change scope without explanation?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-ADR — ADR

**Preferred term:** ADR  
**Russian:** ADR / запись архитектурного решения  
**Status:** approved  
**Concept class:** ADOS architecture concept  
**Genus:** Architecture Decision Record  
**Differentia:** records the context, accepted decision, alternatives, consequences, status, and scope of one material architecture choice

**Definition:** An ADR is a durable record of one material architecture decision.

**Scope note:** Explanatory doctrine remains in `doc/`; ADRs state what this Project adopts, changes, or rejects.

**Must not mean:**
- methodology document
- change log
- all project knowledge

**Cardinality / use rule:** One ADR records one primary decision and has one stable ID.

**Related terms:** PDD, Glossary, doc/, Architecture

**Auditor use:** Trace why conceptual or structural choices changed across versions.

**Drift checks:**
- Is the decision still active?
- Did implementation contradict it?

**Source/adaptation note:** Adapted from ADOS Glossary ADR methodology and current v0.2 agreement.

### TERM-EVIDENCE-LEDGER — Evidence Ledger

**Preferred term:** Evidence Ledger  
**Russian:** журнал доказательств  
**Status:** approved  
**Concept class:** ADOS evidence concept  
**Genus:** append-only logical evidence record  
**Differentia:** records material facts, checks, claims, risks, decisions, and outcomes with traceable source context

**Definition:** An Evidence Ledger is an ADOS trace surface for evidence used to support Project, work, QA, or Delivery claims.

**Scope note:** The auditor evaluates an Evidence Ledger when present but does not require one from every Project or from the evaluating agent.

**Must not mean:**
- proof by itself
- Execution Trace
- mandatory auditor output

**Cardinality / use rule:** A Project may have zero or more physical evidence files representing one logical Evidence Ledger.

**Related terms:** Claim, QA Evidence, Execution Trace, Project

**Auditor use:** Assess evidence traceability without making ledger presence a quality proxy.

**Drift checks:**
- Do entries resolve to actual evidence?
- Are PASS claims broader than ledger content?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile v1.23; optionality added.

### TERM-EXECUTION-TRACE — Execution Trace

**Preferred term:** Execution Trace  
**Russian:** трасса исполнения  
**Status:** approved  
**Concept class:** ADOS evidence concept  
**Genus:** ordered record of visible execution events  
**Differentia:** records commands, actions, decisions, state changes, tool interactions, or results relevant to reconstructing work

**Definition:** An Execution Trace is an ordered ADOS record of visible execution events.

**Scope note:** It may be a log, transcript, event stream, or structured report. It does not include hidden chain-of-thought.

**Must not mean:**
- Evidence Ledger
- Work itself
- complete truth by definition

**Cardinality / use rule:** A build may have zero or more trace artifacts normalized as one evaluated trace surface.

**Related terms:** Building Agent Work, QA Evidence, Evidence Ledger

**Auditor use:** Assess execution transparency and locate stage drift.

**Drift checks:**
- Can material changes be reconstructed?
- Does the trace support the agent's claims?

**Source/adaptation note:** Adapted from ADOS evidence and trajectory concepts in v1.23.

### TERM-QA-EVIDENCE — QA Evidence

**Preferred term:** QA Evidence  
**Russian:** QA-доказательство  
**Status:** approved  
**Concept class:** ADOS evidence concept  
**Genus:** Evidence of a defined quality check  
**Differentia:** records target, criteria, method, outcome, and relevant context for validation, test, review, schema, or quality assessment

**Definition:** QA Evidence is evidence produced by a defined quality-assessment activity.

**Scope note:** A log line or status word without target and criteria is not sufficient QA Evidence.

**Must not mean:**
- test name alone
- Claim
- release acceptance by itself

**Cardinality / use rule:** One QA Evidence item may support one or more bounded Claims when scope is explicit.

**Related terms:** Verify Directive, Claim, Evidence Ledger, Metric

**Auditor use:** Assess whether quality conclusions are supported and correctly scoped.

**Drift checks:**
- What was checked?
- Could the result pass without testing the claimed property?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

## Project Archetypes

### TERM-APP-ARCHETYPE — App Archetype

**Preferred term:** App Archetype  
**Russian:** архетип приложения  
**Status:** approved  
**Concept class:** ADOS Archetype concept  
**Genus:** Archetype  
**Differentia:** classifies a Project whose primary Delivery is an application, service, interface, workflow, command, or automation surface

**Definition:** App Archetype applies when the primary Project Delivery is application-like.

**Scope note:** Business App means App Archetype plus Business Domain, not a separate universal Archetype.

**Must not mean:**
- Domain
- every Project using code
- Runtime Archetype

**Cardinality / use rule:** One evaluation may select App as its primary Archetype.

**Related terms:** Archetype, Project, Build Result, Business Domain

**Auditor use:** Focus evaluation on user-visible behavior, requirements, interfaces, reliability, and delivery fitness.

**Drift checks:**
- Does the result function as the intended app?
- Did app-specific rules leak into non-app Projects?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-RESEARCH-ARCHETYPE — Research Archetype

**Preferred term:** Research Archetype  
**Russian:** архетип исследования  
**Status:** approved  
**Concept class:** ADOS Archetype concept  
**Genus:** Archetype  
**Differentia:** classifies a Project whose primary Delivery is findings, evidence map, corpus, analysis, experiment, or research report

**Definition:** Research Archetype applies when the main output is knowledge or investigation represented in governed artifacts.

**Scope note:** Science is usually a Domain; Research is the delivery Archetype.

**Must not mean:**
- Science Domain
- every Project with web research
- App Archetype

**Cardinality / use rule:** One evaluation may select Research as its primary Archetype.

**Related terms:** Archetype, Science Domain, Claim, QA Evidence

**Auditor use:** Focus evaluation on source quality, uncertainty, reproducibility, validity, and claim traceability.

**Drift checks:**
- Are findings supported?
- Did later versions overstate uncertainty or evidence?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-RUNTIME-ARCHETYPE — Runtime Archetype

**Preferred term:** Runtime Archetype  
**Russian:** архетип runtime / среды исполнения  
**Status:** approved  
**Concept class:** ADOS Archetype concept  
**Genus:** Archetype  
**Differentia:** classifies a Project whose primary Delivery is an execution, build, test, sandbox, orchestration, or operational runtime surface

**Definition:** Runtime Archetype applies when the deliverable is an environment or capability for executing, building, testing, or orchestrating work.

**Scope note:** Runtime Archetype is project type; runtime instance is operating context.

**Must not mean:**
- App Archetype
- runtime instance
- Build Package

**Cardinality / use rule:** One evaluation may select Runtime as its primary Archetype.

**Related terms:** Archetype, Skill, Flow, Build Result

**Auditor use:** Focus evaluation on replayability, behavior, boundaries, interfaces, state, and failure handling.

**Drift checks:**
- Does the runtime perform its declared capability?
- Did proof rely on hidden external state?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-PROFILE-ARCHETYPE — Profile Archetype

**Preferred term:** Profile Archetype  
**Russian:** архетип профиля  
**Status:** approved  
**Concept class:** ADOS Archetype concept  
**Genus:** Archetype  
**Differentia:** classifies a Project whose primary Delivery is a profile, glossary, schema pack, doctrine, policy, or governed configuration

**Definition:** Profile Archetype applies when the primary output defines meaning, expectations, or operating rules for other work.

**Scope note:** A profile may contain runtime guidance but is not automatically Runtime Archetype.

**Must not mean:**
- user preferences only
- Prompt Archetype
- Domain

**Cardinality / use rule:** One evaluation may select Profile as its primary Archetype.

**Related terms:** Archetype, ADOS Profile, Glossary, Schema

**Auditor use:** Focus evaluation on semantic integrity, authority, consistency, applicability, and downstream interpretability.

**Drift checks:**
- Are human and machine surfaces synchronized?
- Did structure increase while meaning weakened?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3.

### TERM-PROMPT-ARCHETYPE — Prompt Archetype

**Preferred term:** Prompt Archetype  
**Russian:** архетип промпта  
**Status:** approved  
**Concept class:** ADOS Archetype concept  
**Genus:** Archetype  
**Differentia:** classifies a Project whose primary Delivery is a controlled Prompt, prompt pack, prompt system, or prompt-governed interaction contract

**Definition:** Prompt Archetype applies when the principal deliverable is a Prompt artifact or prompt system.

**Scope note:** Projects that merely use prompts remain classified by their actual primary Delivery.

**Must not mean:**
- every AI Project
- Directive
- Skill by default

**Cardinality / use rule:** One evaluation may select Prompt as its primary Archetype.

**Related terms:** Archetype, Prompt, Directive, Skill

**Auditor use:** Focus evaluation on instruction clarity, scope, robustness, examples, output contracts, and drift.

**Drift checks:**
- Does the Prompt guide the intended behavior?
- Did corrections bloat or contradict the original Intent?

**Source/adaptation note:** Adapted from ADOS Glossary v1.3 and ADOS Profile prompt concepts.

### TERM-OTHER-ARCHETYPE — Other Archetype

**Preferred term:** Other Archetype  
**Russian:** прочий архетип  
**Status:** approved  
**Concept class:** ADOS Archetype concept  
**Genus:** Archetype  
**Differentia:** is the explicit fallback when App, Research, Runtime, Profile, and Prompt do not adequately describe the primary Delivery

**Definition:** Other Archetype is the fallback project-shape classification.

**Scope note:** Use only with a rationale explaining why specialized Archetypes are unsuitable.

**Must not mean:**
- unknown without analysis
- mixed label
- Domain

**Cardinality / use rule:** One evaluation may select Other as its primary Archetype.

**Related terms:** Archetype, Project, Domain

**Auditor use:** Avoid forcing Projects into inappropriate profiles.

**Drift checks:**
- Was a more specific Archetype available?
- What evaluation risks require custom handling?

**Source/adaptation note:** Project-specific concept created for this auditor.

## Primary Domains

### TERM-BUSINESS-DOMAIN — Business Domain

**Preferred term:** Business Domain  
**Russian:** бизнес-домен  
**Status:** approved  
**Concept class:** ADOS Domain concept  
**Genus:** Domain  
**Differentia:** concerns organizations, customers, operations, products, services, revenue, cost, or business process

**Definition:** Business Domain is the subject-area profile that concerns organizations, customers, operations, products, services, revenue, cost, or business process.

**Scope note:** Use with any Archetype; focus evaluation on business value, workflow fit, stakeholders, economics, and operational risk.

**Must not mean:**
- Archetype
- workflow type
- unexplained fallback

**Cardinality / use rule:** One Intent may select this as its primary Domain.

**Related terms:** Domain, Archetype, Metric, Problem Pattern

**Auditor use:** Apply domain-specific interpretation for business value, workflow fit, stakeholders, economics, and operational risk.

**Drift checks:**
- Were domain constraints represented?
- Was evidence adequate for this Domain?

**Source/adaptation note:** Project-specific Domain profile derived from ADOS Profile v1.23 Domain doctrine.

### TERM-SCIENCE-DOMAIN — Science Domain

**Preferred term:** Science Domain  
**Russian:** научный домен  
**Status:** approved  
**Concept class:** ADOS Domain concept  
**Genus:** Domain  
**Differentia:** concerns scientific inquiry, hypotheses, experiments, models, observations, reproducibility, and falsifiability

**Definition:** Science Domain is the subject-area profile that concerns scientific inquiry, hypotheses, experiments, models, observations, reproducibility, and falsifiability.

**Scope note:** Use with any Archetype; focus evaluation on source quality, methods, uncertainty, reproducibility, and scientific validity.

**Must not mean:**
- Archetype
- workflow type
- unexplained fallback

**Cardinality / use rule:** One Intent may select this as its primary Domain.

**Related terms:** Domain, Archetype, Metric, Problem Pattern

**Auditor use:** Apply domain-specific interpretation for source quality, methods, uncertainty, reproducibility, and scientific validity.

**Drift checks:**
- Were domain constraints represented?
- Was evidence adequate for this Domain?

**Source/adaptation note:** Project-specific Domain profile derived from ADOS Profile v1.23 Domain doctrine.

### TERM-BUSINESS-TRADING-DOMAIN — Business-Trading Domain

**Preferred term:** Business-Trading Domain  
**Russian:** бизнес-трейдинг домен  
**Status:** approved  
**Concept class:** ADOS Domain concept  
**Genus:** Domain  
**Differentia:** concerns markets, trading, portfolio decisions, execution, risk, liquidity, regulation, and financial performance

**Definition:** Business-Trading Domain is the subject-area profile that concerns markets, trading, portfolio decisions, execution, risk, liquidity, regulation, and financial performance.

**Scope note:** Use with any Archetype; focus evaluation on risk-adjusted performance, market assumptions, data quality, compliance, and irreversible actions.

**Must not mean:**
- Archetype
- workflow type
- unexplained fallback

**Cardinality / use rule:** One Intent may select this as its primary Domain.

**Related terms:** Domain, Archetype, Metric, Problem Pattern

**Auditor use:** Apply domain-specific interpretation for risk-adjusted performance, market assumptions, data quality, compliance, and irreversible actions.

**Drift checks:**
- Were domain constraints represented?
- Was evidence adequate for this Domain?

**Source/adaptation note:** Project-specific Domain profile derived from ADOS Profile v1.23 Domain doctrine.

### TERM-EDUCATION-DOMAIN — Education Domain

**Preferred term:** Education Domain  
**Russian:** образовательный домен  
**Status:** approved  
**Concept class:** ADOS Domain concept  
**Genus:** Domain  
**Differentia:** concerns learning objectives, instruction, assessment, curriculum, learners, and educational outcomes

**Definition:** Education Domain is the subject-area profile that concerns learning objectives, instruction, assessment, curriculum, learners, and educational outcomes.

**Scope note:** Use with any Archetype; focus evaluation on pedagogy, accuracy, learner fit, assessment validity, accessibility, and progression.

**Must not mean:**
- Archetype
- workflow type
- unexplained fallback

**Cardinality / use rule:** One Intent may select this as its primary Domain.

**Related terms:** Domain, Archetype, Metric, Problem Pattern

**Auditor use:** Apply domain-specific interpretation for pedagogy, accuracy, learner fit, assessment validity, accessibility, and progression.

**Drift checks:**
- Were domain constraints represented?
- Was evidence adequate for this Domain?

**Source/adaptation note:** Project-specific Domain profile derived from ADOS Profile v1.23 Domain doctrine.

### TERM-SOFTWARE-ENGINEERING-DOMAIN — Software-Engineering Domain

**Preferred term:** Software-Engineering Domain  
**Russian:** домен программной инженерии  
**Status:** approved  
**Concept class:** ADOS Domain concept  
**Genus:** Domain  
**Differentia:** concerns software architecture, code, APIs, testing, deployment, maintainability, security, and operations

**Definition:** Software-Engineering Domain is the subject-area profile that concerns software architecture, code, APIs, testing, deployment, maintainability, security, and operations.

**Scope note:** Use with any Archetype; focus evaluation on technical correctness, compatibility, maintainability, testing, security, and deployment fitness.

**Must not mean:**
- Archetype
- workflow type
- unexplained fallback

**Cardinality / use rule:** One Intent may select this as its primary Domain.

**Related terms:** Domain, Archetype, Metric, Problem Pattern

**Auditor use:** Apply domain-specific interpretation for technical correctness, compatibility, maintainability, testing, security, and deployment fitness.

**Drift checks:**
- Were domain constraints represented?
- Was evidence adequate for this Domain?

**Source/adaptation note:** Project-specific Domain profile derived from ADOS Profile v1.23 Domain doctrine.

### TERM-GOVERNANCE-DOMAIN — Governance Domain

**Preferred term:** Governance Domain  
**Russian:** домен управления и нормативности  
**Status:** approved  
**Concept class:** ADOS Domain concept  
**Genus:** Domain  
**Differentia:** concerns policies, authority, compliance, decision rights, controls, auditability, and institutional rules

**Definition:** Governance Domain is the subject-area profile that concerns policies, authority, compliance, decision rights, controls, auditability, and institutional rules.

**Scope note:** Use with any Archetype; focus evaluation on authority clarity, consistency, applicability, traceability, and control effectiveness.

**Must not mean:**
- Archetype
- workflow type
- unexplained fallback

**Cardinality / use rule:** One Intent may select this as its primary Domain.

**Related terms:** Domain, Archetype, Metric, Problem Pattern

**Auditor use:** Apply domain-specific interpretation for authority clarity, consistency, applicability, traceability, and control effectiveness.

**Drift checks:**
- Were domain constraints represented?
- Was evidence adequate for this Domain?

**Source/adaptation note:** Project-specific Domain profile derived from ADOS Profile v1.23 Domain doctrine.

### TERM-OTHER-DOMAIN — Other Domain

**Preferred term:** Other Domain  
**Russian:** прочий домен  
**Status:** approved  
**Concept class:** ADOS Domain concept  
**Genus:** Domain  
**Differentia:** is used when the subject area does not fit the defined primary Domains

**Definition:** Other Domain is the subject-area profile that is used when the subject area does not fit the defined primary Domains.

**Scope note:** Use with any Archetype; focus evaluation on explicit custom constraints, terminology, evidence expectations, and failure modes.

**Must not mean:**
- Archetype
- workflow type
- unexplained fallback

**Cardinality / use rule:** One Intent may select this as its primary Domain.

**Related terms:** Domain, Archetype, Metric, Problem Pattern

**Auditor use:** Apply domain-specific interpretation for explicit custom constraints, terminology, evidence expectations, and failure modes.

**Drift checks:**
- Were domain constraints represented?
- Was evidence adequate for this Domain?

**Source/adaptation note:** Project-specific Domain profile derived from ADOS Profile v1.23 Domain doctrine.

## ADOS Pillar Set

The following list adapts the twenty pillars from ADOS Profile v1.23. Pillar doctrine is static; applicability depends on the selected Project, Archetype, Domain, and evaluation scope. `PILLAR-01` is generalized from app/project classification to Project classification.

| Pillar ID | Name | v0.2 adapted meaning |
|---|---|---|
| PILLAR-01 | Project Classification | Classify the work as app, research, runtime, profile, prompt, other, or a justified custom form before selecting evaluation emphasis. |
| PILLAR-02 | Archetype and Domain Grounding | Separate reusable Project Archetype from the subject-matter Domain. |
| PILLAR-03 | Goal Figure and Objective Formation | Define the target state and material Objectives before evaluating implementation details. |
| PILLAR-04 | Goal-Attractor Geometry | Represent Semantic Meaning Space, Coordinate Dimensions, Goal Surface, Goal Attractor, acceptable variation, and convergence. |
| PILLAR-05 | Requirements Applicability | Apply only Requirements relevant to the selected Project, Archetype, Domain, risk, and delivery scope. |
| PILLAR-06 | Traceability and Test Pressure | Connect active Requirements and quality Claims to inspectable evaluation or evidence routes. |
| PILLAR-07 | Authority Ownership | Assign each durable concept, rule, schema, and evidence surface to one clear authority. |
| PILLAR-08 | Compaction | Minimize duplicated prose, generated clutter, and unnecessary surfaces while preserving sufficient meaning and proof. |
| PILLAR-09 | Schema-Backed Data Discipline | Represent governed structured data with explicit JSON schemas where machine structure is valuable. |
| PILLAR-10 | Specification First | Define intended objects, boundaries, constraints, and acceptance meaning before material mutation. |
| PILLAR-11 | Evidence and Execution Traceability | Make material decisions, checks, risks, fixes, and claims auditable from visible evidence. |
| PILLAR-12 | Semantic Reflection | Evaluate whether the Project still moves toward the active Goal Surface rather than merely passing structural checks. |
| PILLAR-13 | Execution State Materialization | Materialize important execution state when the selected Project model requires durable traceability. |
| PILLAR-14 | Self-Evaluation Creation | Create Project-local quality assessment from geometry, applicable coordinates, metrics, and evidence when applicable. |
| PILLAR-15 | Fixtures and Regression Sentinels | Use compact representative fixtures for critical regressions and known failure modes without overgeneralizing them. |
| PILLAR-16 | Host Runtime Boundaries | Separate portable Package responsibilities from host-dependent runtime capabilities and conditions. |
| PILLAR-17 | Document Governance | Use metadata, clear authority roles, routing guidance, and document contracts. |
| PILLAR-18 | Workflow Tier and Execution Budget | Select the smallest sufficient execution or evaluation burden for the Project's risk and evidence needs. |
| PILLAR-19 | ADOS Compliance Verification | Assess material ADOS alignment beyond a local self-reported validator result. |
| PILLAR-20 | Language Maturity and Normative Vocabulary | Use mature, precise, Domain-aligned vocabulary and reserve normative language for actual authority. |

## Core-file content principles

| File | Owns | Must not own |
|---|---|---|
| `PACKAGE.json` | Machine identity, version, Goal, Objectives, semantic authority, entrypoints, methodology sources, and non-goals. | Full glossary definitions, report results, or agent execution governance. |
| `MANIFEST.md` | Agent load order, authority map, package-surface roles, and navigation. | Semantic redefinitions, full Project definition, or mandatory builder workflow. |
| `README.md` | Human overview, product boundary, usage, and major entrypoints. | Binding concept definitions, detailed architecture decisions, or numeric evaluation authority. |
| `GLOSSARY.md` | Approved concept meanings, boundaries, relations, and drift guards. | Per-project findings or release history. |
| `PDD.md` | This Project's Goal, Objectives, scope, architecture boundaries, and accepted Delivery meaning. | General ADOS doctrine already owned by the Glossary or `doc/`. |

## Source methodology

- ADOS Glossary v1.3 supplied the concept-oriented glossary method, term boundaries, ontology/taxonomy method, competency questions, metadata model, and distinction between instruction, work, evidence, and delivery.
- ADOS Profile v1.23 supplied the Pillar Set, Semantic Meaning Space, Goal-Attractor Geometry, Coordinate Dimension, Metric, Archetype, Domain, and requirement-doctrine concepts.
- App-specific source terms were reviewed. `Project Requirement` is used as the general concept; App-specific requirements remain possible only inside the App Archetype.
