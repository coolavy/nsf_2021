def split_lines(a, split_length=10):
    index = 0
    result = []
    while index < len(a):
        result.append(a[index: index+split_length])
        index = index + split_length
    return result

a = "janvinabniparujvnvpjidhnfpaiujfnpajvinparvhifndapanhpvapruhbgpadff;f"
result = split_lines(a, 15)
print(result)
