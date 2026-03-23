# Test Coverage Results

## Task
The task was to improve the test coverage of `prep.py` by adding more test cases to `tests/test_prep.py`.

## What I did
I added test cases for all six possible behaviours of `strange_function(a, b, c, d)` in test_prep.py

Each test was written to make the function go through a different branch of the conditional logic.

## Coverage before
The initial coverage of `prep.py` was 33%.

## Coverage after
After adding the new test cases, the coverage of `prep.py` became 100%.

## Why this matters
This improves regression testing because all return paths of the function are now tested. If someone changes the function later and breaks one of these behaviours, the tests should catch it. 

