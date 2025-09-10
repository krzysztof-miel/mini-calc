#!/bin/bash
locust -f perf/locustfile.py --headless \
  -u 10 -r 5 -t 20s \
  --csv=reports/perf/locust --only-summary
