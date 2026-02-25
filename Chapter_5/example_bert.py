from bert_score import score

# Log and LLM Summary for evaluation
reference_log = ["level=info ts=2026-02-10T06:51:31.353816972Z caller=controller.go:195 component=kubelet_endpoints kubelet_object=kube-system/kube-prometheus-stack-1754-kubelet msg=\"Node Ready condition is Unknown\" node=kind-worker3"]
model_summary = ["On Feb 10, 06:51:31Z, the nodes `kind-worker2` and `kind-worker3` had their \"Ready\" condition set to \"Unknown\"."]

P, R, F1 = score(reference_log, model_summary, model_type='distilbert-base-uncased', verbose=False)
print(f"BERTScore F1: {F1[0]:.4f}")
print(f"BERTScore Precision: {P[0]:.4f}")
print(f"BERTScore Recall: {R[0]:.4f}")

