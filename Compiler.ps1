winget install Python.Python.3.11



$sourceFile = "impossiblebot.py"
$outputName = "impossiblebot.exe"
pyinstaller --onefile --windowed --name $outputName $sourceFile

# Remove spec file
Remove-Item -Path "$outputName.spec"

$sourceFile = "mediumbot.py"
$outputName = "mediumbot.exe"
pyinstaller --onefile --windowed --name $outputName $sourceFile

# Remove spec file
Remove-Item -Path "$outputName.spec"

$sourceFile = "easybot.py"
$outputName = "easybot.exe"
pyinstaller --onefile --windowed --name $outputName $sourceFile

# Remove spec file
Remove-Item -Path "$outputName.spec"

