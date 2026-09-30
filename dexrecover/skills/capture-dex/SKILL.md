# capture-dex

Goal: obtain or import a runtime DEX capture from an owned/authorized Android target, with a clear event label.

Keep the scope to DEX acquisition. Prefer controlled events such as "before login" and "after opening feature X" over blind periodic dumping.

Output should be a capture directory or normalized capture manifest suitable for `dexrecover scan`.
