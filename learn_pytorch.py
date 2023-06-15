import torch

# x = torch.empty(3, 2, 3)
# print(x)

# # Create tensor with random values
# x = torch.rand(2, 3)
# print(x)

# # Creat tensor with value 0
# x = torch.zeros(2, 3)
# print(x)

# # Creat tensor with value 1
# x = torch.ones(2, 3)
# print(x)

# # Give data type
# x = torch.ones(2, 2, dtype=torch.int)
# print(x.dtype)

# Take the size of tensor
x = torch.ones(2, 2, dtype=torch.float64)
print(x.size())