#training loops

#Batch processing
dataset_size=1000000
batch_size=200

num_batches=dataset_size//batch_size
for batch_num in range(num_batches):
    start_idx=batch_num*batch_size
    end_idx=start_idx+batch_size
print(f"Processing batch {batch_num+1}: samples{start_idx} to {end_idx}")

