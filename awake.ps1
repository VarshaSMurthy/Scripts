param($minutes = 760)

$myshell = New-Object -com "Wscript.Shell"

for ($i = 0; $i -lt $minutes; $i++) {
  Start-Sleep -Seconds 90
  $myshell.sendkeys(".")
}
