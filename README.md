# Removedor de Marca d'Água (APK)

Este é um aplicativo Android para remover marcas d'água de vídeos, desenvolvido com **Kivy** e **Python**. O aplicativo permite que o usuário selecione um vídeo, aplique um blur na área da marca d'água e salve o vídeo processado.

## Funcionalidades
- Seleção de vídeos do dispositivo.
- Aplicação de blur em áreas específicas.
- Exportação do vídeo processado com áudio.

## Pré-requisitos
- Python 3.8 ou superior.
- Kivy.
- OpenCV.
- MoviePy.
- Buildozer (para compilar o APK).

## Como Compilar o APK

### 1. Instale as dependências
```bash
pip install kivy buildozer opencv-python moviepy
```

### 2. Clone este repositório
```bash
git clone https://github.com/mgrprogrmador173-arch/removedor-marca-dagua-apk.git
cd removedor-marca-dagua-apk
```

### 3. Compile o APK
```bash
buildozer init
buildozer android debug
```

### 4. Instale o APK
Após a compilação, o APK estará em `bin/removedormarcadagua-0.1-debug.apk`. Transfira o arquivo para o seu dispositivo Android e instale.

## Observações
- O aplicativo foi testado em dispositivos Android com API 21 ou superior.
- Certifique-se de que o dispositivo tem permissão para instalar aplicativos de fontes desconhecidas.

## Licença
Este projeto é de uso livre para fins educacionais e pessoais.