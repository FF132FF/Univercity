import ScikitKMeansCompressor

requestedFile = "input.jpg"
K = int(input("  Введите количество цветов: "))
print("===========")
maxIters = int(input("  Введите количество итераций: "))
print("===========")

ScikitKMeansCompressor.Compressor(requestedFile, K, maxIters)