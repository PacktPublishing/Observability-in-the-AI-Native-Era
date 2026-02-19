# Import evaluate 
import evaluate

# ROUGE
rouge_calculation = evaluate.load("rouge")

# Example data to score. It should be plain text (Not tokens)
reference_log = ["level=info ts=2026-02-10T06:51:31.353816972Z caller=controller.go:195 component=kubelet_endpoints kubelet_object=kube-system/kube-prometheus-stack-1754-kubelet msg=\"Node Ready condition is Unknown\" node=kind-worker3"]
model_summary = ["On Feb 10, 06:51:31Z, the nodes `kind-worker2` and `kind-worker3` had their \"Ready\" condition set to \"Unknown\"."]

# ROUGE expects plain text inputs
rouge_score = rouge_calculation.compute(predictions=model_summary, references=reference_log)

# Access ROUGE scores (no need for indexing into the result)
print(f"ROUGE-1 F1 Score: {rouge_score['rouge1']:.2f}")
print(f"ROUGE-LSum F1 Score: {rouge_score['rougeLsum']:.2f}")