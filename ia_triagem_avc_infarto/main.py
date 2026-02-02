from ia_triagem_avc_infarto.audio_analysis import analyze_audio
from ia_triagem_avc_infarto.text_analysis import analyze_text
from ia_triagem_avc_infarto.models.risk_model import calculate_risk

def main():
    print("=== IA DE TRIAGEM PREVENTIVA (AVC / INFARTO) ===")

    audio_path = input("Caminho do arquivo de áudio (.wav): ")
    text_input = input("Digite um pequeno texto: ")

    audio_features = analyze_audio(audio_path)
    text_features = analyze_text(text_input)

    result = calculate_risk(audio_features, text_features)

    print("\n--- RESULTADO DA TRIAGEM ---")
    print(result)

if __name__ == "__main__":
    main()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
