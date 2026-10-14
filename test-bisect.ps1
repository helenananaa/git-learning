$content = Get-Content calc.txt

if ($content -eq "result=42") {
    exit 0
} else {
    exit 1
}
