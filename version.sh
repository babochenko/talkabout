find . -type f -exec perl -i -pe '
  s/\b(0\.1\.)(\d+)\b/"$1" . ($2 + 1)/ge
' {} +

