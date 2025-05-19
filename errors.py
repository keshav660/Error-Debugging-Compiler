# # 2. errors.py (Error Detection + GPT AI Integration)

# import openai

# openai.api_key = "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"  # Replace with your key
# # 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
# def check_errors(code):
#     errors = []
#     lines = code.split("\n")

#     has_main = any("main(" in line for line in lines)
#     open_parens = 0
#     close_parens = 0

#     for i, line in enumerate(lines):
#         stripped = line.strip()
#         open_parens += stripped.count('(')
#         close_parens += stripped.count(')')

#         if not stripped or stripped.startswith("//"):
#             continue

#         keywords = ["printf", "scanf", "return", "int", "char", "float", "double"]
#         if any(kw in stripped for kw in keywords):
#             if not stripped.endswith(";") and not stripped.endswith("{") and not stripped.endswith("}"):
#                 errors.append({
#                     "line": i + 1,
#                     "error": "Possibly missing semicolon.",
#                     "suggestion": stripped + ";"
#                 })

#     if open_parens != close_parens:
#         errors.append({
#             "line": "-",
#             "error": f"Mismatched parentheses: {open_parens} '(' vs {close_parens} ')'",
#             "suggestion": "Check all opening and closing parentheses."
#         })

#     if not has_main:
#         errors.append({
#             "line": "-",
#             "error": "Missing main() function.",
#             "suggestion": "Add: int main() { /* code */ }"
#         })

#     # 🔍 AI-Powered Suggestions (Optional for detailed explanation)
#     gpt_prompt = f"Analyze this C code and provide syntax issues with suggestions:\n\n{code}"

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "user", "content": gpt_prompt}
#             ],
#             temperature=0.2
#         )
#         gpt_output = response['choices'][0]['message']['content']
#         errors.append({
#             "line": "AI",
#             "error": "AI Suggestions",
#             "suggestion": gpt_output
#         })
#     except Exception as e:
#         errors.append({
#             "line": "AI",
#             "error": "AI Analysis Failed",
#             "suggestion": str(e)
#         })

#     return errors


import openai

# Toggle this flag to switch AI integration ON or OFF
USE_AI = False

# OpenAI API Key (keep secure in real project)
openai.api_key = "sk-proj-..."  # Replace with working key or keep hidden for demo

def check_errors(code):
    errors = []
    lines = code.split("\n")

    has_main = any("main(" in line for line in lines)
    open_parens = 0
    close_parens = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        open_parens += stripped.count('(')
        close_parens += stripped.count(')')

        if not stripped or stripped.startswith("//"):
            continue

        keywords = ["printf", "scanf", "return", "int", "char", "float", "double"]
        if any(kw in stripped for kw in keywords):
            if not stripped.endswith(";") and not stripped.endswith("{") and not stripped.endswith("}"):
                errors.append({
                    "line": i + 1,
                    "error": "Possibly missing semicolon.",
                    "suggestion": stripped + ";"
                })

    if open_parens != close_parens:
        errors.append({
            "line": "-",
            "error": f"Mismatched parentheses: {open_parens} '(' vs {close_parens} ')'",
            "suggestion": "Check all opening and closing parentheses."
        })

    if not has_main:
        errors.append({
            "line": "-",
            "error": "Missing main() function.",
            "suggestion": "Add: int main() { /* code */ }"
        })

    # 🔍 AI-Powered Suggestions
    gpt_prompt = f"Analyze this C code and provide syntax issues with suggestions:\n\n{code}"

    if USE_AI:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": gpt_prompt}
                ],
                temperature=0.2
            )
            gpt_output = response['choices'][0]['message']['content']
            errors.append({
                "line": "AI",
                "error": "AI Suggestions",
                "suggestion": gpt_output
            })
        except Exception as e:
            errors.append({
                "line": "AI",
                "error": "AI Analysis Failed",
                "suggestion": str(e)
            })
    else:
        # Static sample output for demo purposes
        sample_ai_output = (
            "- Line 4: Missing semicolon after `return 0`\n"
            "- Line 7: Suspicious function call without parentheses\n"
            "Suggestion: Always use correct syntax and close blocks properly."
        )
        errors.append({
            "line": "AI",
            "error": "Sample AI Suggestions (Offline Mode)",
            "suggestion": sample_ai_output
        })

    return errors
