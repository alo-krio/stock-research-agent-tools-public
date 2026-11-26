# Evaluate a research agent

**Inputs.** A frozen document packet and questions with independently checked answers.

1. Give each agent the same evidence cutoff, tool access and question set. Record the model and prompt version.
2. Evaluate factual accuracy, cited passage, units and fiscal period separately. Include questions that the packet cannot answer.
3. Change document order and include stale evidence. Inspect whether answers remain grounded and whether the agent abstains when evidence is missing.

**Acceptance check.** Publish evaluation criteria, aggregate errors and abstention counts. Inspect a sample of cited passages before interpreting an aggregate score.

**Upstream resources.** [FinanceBench](https://huggingface.co/datasets/PatronusAI/financebench) · [promptfoo](https://github.com/promptfoo/promptfoo) · [Arize Phoenix](https://github.com/Arize-ai/phoenix)
