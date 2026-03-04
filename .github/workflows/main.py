name: Auto Trigger Semaphore
on:
  schedule:
    - cron: '*/30 * * * *'
  workflow_dispatch:

jobs:
  push_to_trigger:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout Specific Branch
        uses: actions/checkout@v4
        with:
          ref: set-up-semaphore # <--- WAJIB TAMBAHKAN INI

      - name: Create Empty Commit
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          # Membuat perubahan kecil pada file atau commit kosong
          git commit --allow-empty -m "Trigger Semaphore on set-up-branch: $(date)"
          git push origin set-up-semaphore # <--- PASTIKAN PUSH KE BRANCH YG BENAR
