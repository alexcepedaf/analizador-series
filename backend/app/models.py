from datetime import datetime, timezone

class NumberSeries: 
    def __init__(self, numbers):
        self.numbers = numbers
        self.count = len(numbers)
        self.created_at = datetime.now(timezone.utc)

class AnalysisResult:
    def __init__(self,series_id, gcd, mean, std_dev, primes):
        self.series_id = series_id
        self.gcd = gcd
        self.mean = mean
        self.std_dev = std_dev
        self.primes = primes