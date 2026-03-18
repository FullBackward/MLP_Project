from datasets import load_dataset

ds = load_dataset("mueller91/MLAAD")

ds.save_to_disk("MLAAD_local")
