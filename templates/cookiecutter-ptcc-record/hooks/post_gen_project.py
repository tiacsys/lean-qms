folder_name = "{{ cookiecutter.__folder_name }}"
full_name = "{{ cookiecutter.__full_name }}"

print()
print(f"Created {folder_name}/")
print()
print("Next steps:")
print("  1. Review the generated record, especially the GPG fingerprint block.")
print("  2. Register the new sub-project in documents.yaml (repo root), under the 'records' group:")
print()
print(f"       {folder_name}:")
print(f'         title: "PTCC - {full_name}"')
print("         group: records")
print()
print(f"  3. Build it: ./build.py html {folder_name}")
print("  4. Sign and commit per SOP-DOCCTL's Git Commit Requirements (signed, verified commit).")
print()
