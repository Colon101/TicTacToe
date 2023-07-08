# Install required Python packages
$packages = @(
    "tk",
    "random",
    "pyinstaller"
)

foreach ($package in $packages) {
    Write-Host "Installing $package..."
    pip install $package
}