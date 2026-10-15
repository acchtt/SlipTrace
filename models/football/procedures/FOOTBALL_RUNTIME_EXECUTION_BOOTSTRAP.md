# Football runtime execution bootstrap

The active runtime is deliberately thin.

## Active execution

Football C is the only active model.

Use:

python models/football/engine/xi_portable.py self-check
python models/football/engine/xi_portable.py xi --c c_football.json

The runner imports the real shared core.py and adapter.py. There is no source
transport bootstrap, embedded model blob, pair runner or shadow-model runtime.

Optional current-price execution uses --price-c. A user screenshot uses
--screenshot-quote and remains non-executable evidence.

C2/C3/C4 are retired. Old pair-runner files may remain for historical source
traceability but are not production dependencies and must not be imported by
active launchers or CI.
