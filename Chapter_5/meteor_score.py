import nltk
from nltk.translate.meteor_score import meteor_score
nltk.download('wordnet')

reference_log = "level=info ts=2026-02-10T06:51:31.353816972Z caller=controller.go:195 component=kubelet_endpoints kubelet_object=kube-system/kube-prometheus-stack-1754-kubelet msg=\"Node Ready condition is Unknown\" node=kind-worker3"
model_summary = "On Feb 10, 06:51:31Z, the nodes `kind-worker2` and `kind-worker3` had their \"Ready\" condition set to \"Unknown\"."

# meteor_score expects pre-tokenized inputs (lists of words)
# references: list of tokenized reference sentences, hypothesis: tokenized hypothesis
score: float = meteor_score([
    reference_log.split()
], model_summary.split())

print(f"Reference: {reference_log}")
print(f"Candidate: {model_summary}")
print(f"METEOR score: {score:.4f}")