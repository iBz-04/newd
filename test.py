from newd import detect


# Try with a lower threshold
print("\nResults with lower threshold (0.3):")
results = detect('image.jpg', min_prob=0.3)
print(results)

# For faster detection with slightly lower accuracy and lower threshold
print("\nResults with fast mode and lower threshold:")
results = detect('image.jpg', mode="fast", min_prob=0.3)
print(results)