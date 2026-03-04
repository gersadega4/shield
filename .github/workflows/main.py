name: Auto Trigger Semaphore
on:
  schedule:
    - cron: '*/30 * * * *' # Berjalan otomatis setiap 30 menit
  workflow_dispatch:      # Memungkinkan Anda klik tombol "Run" secara manual

jobs:
  push_to_trigger:
    runs-on: ubuntu-latest
    permissions:
      contents: write     # Izin wajib untuk melakukan push
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Create Empty Commit
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git commit --allow-empty -m "Trigger Semaphore: $(date)"
          git push
