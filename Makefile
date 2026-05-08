PY=uv run python
BUILD_SPEC=spec-build

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: bump-major
bump-major:
	$(PY) util/bump_version.py major

.PHONY: bump-minor
bump-minor:
	$(PY) util/bump_version.py minor

.PHONY: bump-patch
bump-patch:
	$(PY) util/bump_version.py patch

LIBSPEC=uv run libspec

.PHONY: spec
spec: 
	$(LIBSPEC) build spec/main_spec.py -o spec-build

.PHONY: diff
diff:
	$(LIBSPEC) diff ./spec-build
