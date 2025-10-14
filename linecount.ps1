
Clear-Host

$stats = Get-ChildItem -Recurse -Filter *.py | Get-Content | Measure-Object -Line -Word -Character
$stats | Select-Object Lines, Words, Characters