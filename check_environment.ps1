# Script de Verificação do Ambiente de Testes
# ============================================
# Verifica se o ambiente está configurado corretamente

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  VERIFICAÇÃO DO AMBIENTE DE TESTES" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$errors = 0
$warnings = 0

# 1. Verificar Python
Write-Host "1. Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($pythonVersion -match "3\.(1[1-9]|[2-9][0-9])") {
        Write-Host "   ✓ Python instalado: $pythonVersion" -ForegroundColor Green
    } else {
        Write-Host "   ✗ Python 3.11+ necessário. Versão atual: $pythonVersion" -ForegroundColor Red
        $errors++
    }
} catch {
    Write-Host "   ✗ Python não encontrado" -ForegroundColor Red
    $errors++
}

# 2. Verificar venv
Write-Host "`n2. Verificando ambiente virtual..." -ForegroundColor Yellow
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "   ✓ Ambiente virtual encontrado" -ForegroundColor Green
    
    # Verificar se está ativado
    if ($env:VIRTUAL_ENV) {
        Write-Host "   ✓ Ambiente virtual ativado" -ForegroundColor Green
    } else {
        Write-Host "   ⚠ Ambiente virtual não está ativado" -ForegroundColor Yellow
        Write-Host "     Execute: .\venv\Scripts\Activate.ps1" -ForegroundColor Yellow
        $warnings++
    }
} else {
    Write-Host "   ✗ Ambiente virtual não encontrado" -ForegroundColor Red
    Write-Host "     Execute: python -m venv venv" -ForegroundColor Red
    $errors++
}

# 3. Verificar dependências
Write-Host "`n3. Verificando dependências..." -ForegroundColor Yellow
$packages = @("selenium", "pytest", "python-dotenv", "webdriver-manager")
foreach ($package in $packages) {
    try {
        $result = pip show $package 2>&1
        if ($LASTEXITCODE -eq 0) {
            $version = ($result | Select-String "Version:").ToString().Split(":")[1].Trim()
            Write-Host "   ✓ $package instalado (v$version)" -ForegroundColor Green
        } else {
            Write-Host "   ✗ $package não instalado" -ForegroundColor Red
            $errors++
        }
    } catch {
        Write-Host "   ✗ Erro ao verificar $package" -ForegroundColor Red
        $errors++
    }
}

# 4. Verificar ChromeDriver
Write-Host "`n4. Verificando ChromeDriver..." -ForegroundColor Yellow
if (Test-Path "C:\chromedriver\chromedriver.exe") {
    try {
        $chromeDriverVersion = & "C:\chromedriver\chromedriver.exe" --version
        Write-Host "   ✓ ChromeDriver encontrado: $chromeDriverVersion" -ForegroundColor Green
    } catch {
        Write-Host "   ✗ Erro ao executar ChromeDriver" -ForegroundColor Red
        $errors++
    }
} else {
    Write-Host "   ✗ ChromeDriver não encontrado em C:\chromedriver\" -ForegroundColor Red
    Write-Host "     Baixe de: https://googlechromelabs.github.io/chrome-for-testing/" -ForegroundColor Red
    $errors++
}

# 5. Verificar arquivo .env
Write-Host "`n5. Verificando configuração..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "   ✓ Arquivo .env encontrado" -ForegroundColor Green
    
    # Verificar variáveis importantes
    $envContent = Get-Content ".env"
    $requiredVars = @("FRONTEND_URL", "CHROME_DRIVER_PATH")
    foreach ($var in $requiredVars) {
        if ($envContent -match $var) {
            Write-Host "   ✓ $var configurado" -ForegroundColor Green
        } else {
            Write-Host "   ⚠ $var não encontrado em .env" -ForegroundColor Yellow
            $warnings++
        }
    }
} else {
    Write-Host "   ⚠ Arquivo .env não encontrado" -ForegroundColor Yellow
    Write-Host "     Execute: cp .env.example .env" -ForegroundColor Yellow
    $warnings++
}

# 6. Verificar frontend
Write-Host "`n6. Verificando frontend..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:5173" -TimeoutSec 2 -UseBasicParsing 2>$null
    Write-Host "   ✓ Frontend está rodando em localhost:5173" -ForegroundColor Green
} catch {
    Write-Host "   ⚠ Frontend não está respondendo em localhost:5173" -ForegroundColor Yellow
    Write-Host "     Inicie o frontend antes de executar os testes" -ForegroundColor Yellow
    $warnings++
}

# Resumo
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  RESUMO DA VERIFICAÇÃO" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

if ($errors -eq 0 -and $warnings -eq 0) {
    Write-Host "✓ Ambiente configurado corretamente!" -ForegroundColor Green
    Write-Host "`nPróximos passos:" -ForegroundColor Cyan
    Write-Host "  1. Ativar venv (se não estiver): .\venv\Scripts\Activate.ps1" -ForegroundColor White
    Write-Host "  2. Executar testes: pytest -v" -ForegroundColor White
} else {
    if ($errors -gt 0) {
        Write-Host "✗ $errors erro(s) encontrado(s)" -ForegroundColor Red
        Write-Host "  Corrija os erros acima antes de executar os testes" -ForegroundColor Red
    }
    if ($warnings -gt 0) {
        Write-Host "⚠ $warnings aviso(s) encontrado(s)" -ForegroundColor Yellow
        Write-Host "  Os avisos podem não impedir a execução dos testes" -ForegroundColor Yellow
    }
}

Write-Host "`n========================================`n" -ForegroundColor Cyan
