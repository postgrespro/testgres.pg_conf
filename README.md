[![CI Status](https://img.shields.io/github/actions/workflow/status/postgrespro/testgres.pg_conf/.github/workflows/ci.yml?label=CI)](https://github.com/postgrespro/testgres.pg_conf/actions/workflows/ci.yml)
[![PyPI package version](https://badge.fury.io/py/testgres_postgres-configuration.svg)](https://badge.fury.io/py/testgres.postgres-configuration)
[![PyPI python versions](https://img.shields.io/pypi/pyversions/testgres_postgres_configuration)](https://pypi.org/project/testgres.postgres-configuration)

# testgres.pg_conf

A robust, enterprise-grade Python library designed for parsing, manipulating, and writing PostgreSQL configuration files. This library functions as a modular component of the `testgres` ecosystem.

## What is it?

`testgres.pg_conf` provides a comprehensive object-oriented interface to manage complex, multi-file PostgreSQL configurations (such as `postgresql.conf` and `postgresql.auto.conf`). It allows developers and QA engineers to programmatically inspect, modify, and save database settings within isolation layers, making it ideal for automated testing infrastructure and database orchestration.

## Key Features

* **Multi-File & Include Directive Support:** Seamlessly loads, traverses, and writes deeply nested configuration structures utilizing `include`, `include_if_exists`, and `include_dir` directives.
* **Preservation of Comments and Formatting:** Built using a dedicated layout tracking engine that preserves human-written inline comments, block comments, blank lines, and file indentation patterns upon serialization.
* **Advanced List-Option Manipulation:** Provides high-level APIs like `SetOptionValueItem` to append items to comma-separated parameters (e.g., `shared_preload_libraries`) uniquely, eliminating string-concatenation errors.
* **Flexible Validation Strategies (`Strict` vs `Standard`):** 
  * `Standard` mode mimics real-world PostgreSQL behavior where parameter overrides and duplicates are allowed ("last definition wins").
  * `Strict` mode enforces single-definition invariants, throwing structured errors when accidental duplicates are detected.
* **Fail-Safe Lifecycle Verification:** Leverages internal `IsAlive` state validation mechanics to safeguard against modifying zombie reference nodes or processing out-of-sync cache handles.
* **Native `TestgresException` Integration:** Features a fully typed, strict hierarchy of operational errors and fatal bug checks derived directly from the core `testgres` exception package.

## Installation

Install the library using `pip`:

```bash
pip install testgres.postgres-configuration
```

## Quick Start Example

The following complete end-to-end example demonstrates how to initialize a temporary cluster via `testgres`, load its configuration, modify scalar and list properties, and verify changes natively using SQL statements.

```python
import testgres
import testgres.postgres_configuration as testgres_pg_conf

# 1. Initialize a standard temporary PostgreSQL node using testgres
node = testgres.PostgresNode()
node.init()

# 2. Attach our configuration manager to the node's data directory (PGDATA)
cfg = testgres_pg_conf.PostgresConfiguration(node.data_dir)

# Load existing configuration files (postgresql.conf, etc.) from disk
testgres_pg_conf.PostgresConfigurationReader.LoadConfiguration(cfg)

# ----------------------------------------------------------------------
# Setup Initial State for List Demonstration
# ----------------------------------------------------------------------
# Let's explicitly define a base preloaded library first
cfg.SetOptionValue("shared_preload_libraries", "auto_explain")

# ----------------------------------------------------------------------
# Demonstration of GetOptionValue (Reading Current Values)
# ----------------------------------------------------------------------
# Read the current port configuration. It retrieves the effective value
# from the configuration tree (handling overrides if multiple exist).
current_port = cfg.GetOptionValue("port")
print(f"Initial PostgreSQL port: {current_port}")

# ----------------------------------------------------------------------
# Demonstration of SetOptionValue (Scalar Options)
# ----------------------------------------------------------------------
# Change the maximum number of concurrent connections from default 100 to 15.
# In 'Standard' mode, this creates or updates the postgresql.auto.conf file.
cfg.SetOptionValue("max_connections", 15)

# ----------------------------------------------------------------------
# Demonstration of SetOptionValueItem (List/Array Options - Appending)
# ----------------------------------------------------------------------
# Unique append: instead of replacing 'auto_explain', this method appends
# 'pg_stat_statements' into the existing list parameter.
cfg.SetOptionValueItem("shared_preload_libraries", "pg_stat_statements")

# ----------------------------------------------------------------------
# Save and Apply Changes
# ----------------------------------------------------------------------
# Flush all modified in-memory configuration trees back to the file system
testgres_pg_conf.PostgresConfigurationWriter.WriteConfiguration(cfg)

# 3. Start the PostgreSQL server to let it pick up the new configuration
node.start()

# 4. Verify modified options via standard SQL queries
# Verify max_connections changes
res_conn = node.execute("SELECT setting FROM pg_settings WHERE name = 'max_connections';")
print(f"Configured max_connections: {res_conn}")  # Output: 15

# Verify preloaded libraries using native SHOW command.
# Output will prove that 'pg_stat_statements' was safely appended to 'auto_explain'.
res_libs = node.execute("SHOW shared_preload_libraries;")
print(f"Preloaded libraries: {res_libs}")  # Expected output: auto_explain,pg_stat_statements

# 5. Stop the process and clean up temporary node directories
node.cleanup()
```

## Authors

[Postgres Professional](https://postgrespro.ru/about)
