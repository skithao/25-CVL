#!/bin/bash

vllm serve ./DeepSeek-R1-Distill-Qwen-1.5B \
  --dtype=half \
  --port 8110 \
  --tensor-parallel-size 1 \
  --max-model-len 2048 \
  --max-num-batched-tokens 2048 \
  --gpu-memory-utilization 0.85 \
  --swap-space 32 \
  --block-size 16 \
  --enforce-eager