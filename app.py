from flask import Flask, request, render_template, session
from crewai import Agent
from langchain_ollama.chat_models import ChatOllama
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed to store results in session

# Ensure Ollama is running: `ollama serve`
llm = ChatOllama(model="openhermes", base_url="http://localhost:11434")

# Define Math AI Agent
math_agent = Agent(
    role="Mathematician AI",
    goal="Solve equations and expressions with detailed explanations.",
    backstory="A skilled mathematician with expertise in algebra, calculus, and functions.",
    allow_delegation=False,
    llm=llm
)

# Solve expressions
def solve_expression(expression):
    try:
        expr = sp.sympify(expression)  
        simplified_expr = expr.simplify()

        explanation_prompt = f"Explain step-by-step how to simplify: {expression}."
        explanation_response = llm.invoke(explanation_prompt)
        explanation_text = explanation_response.content if hasattr(explanation_response, "content") else str(explanation_response)

        steps_html = "".join(f"<li>{step.strip()}</li>" for step in explanation_text.split("\n") if step.strip())

        return f"""
        <div style="text-align:center;">
            <h2><b>Solution:</b> {simplified_expr}</h2>
        </div>
        <h3>Step-by-Step Explanation:</h3>
        <ol>{steps_html}</ol>
        """
    except Exception as e:
        return f"<p style='color:red;'>Error: {e}</p>"

# Solve one or two equations
def solve_equation(equation):
    try:
        x, y = sp.symbols("x y")  
        equations = equation.split(",")  
        parsed_equations = []

        for eq in equations:
            if "=" in eq:
                left_side, right_side = eq.split("=")
                parsed_equations.append(sp.Eq(sp.sympify(left_side.strip()), sp.sympify(right_side.strip())))
            else:
                parsed_equations.append(sp.sympify(eq.strip()))

        if len(parsed_equations) == 1:  
            solution = sp.solve(parsed_equations[0], x)  
        else:  
            solution = sp.solve(parsed_equations, (x, y))  

        solution_str = ", ".join(f"{var} = {val}" for var, val in solution.items()) if isinstance(solution, dict) else str(solution)
        return solution_str
    except Exception as e:
        return f"Error: {e}"

# Generate a graph for one or two equations
def generate_graph(equation):
    try:
        x = sp.Symbol("x")
        y = sp.Symbol("y")
        equations = equation.split(",")  
        colors = ["blue", "red"]  

        x_vals = np.linspace(-10, 10, 400)
        plt.figure(figsize=(6, 4))

        for i, eq in enumerate(equations):
            eq = eq.replace("^", "**")  
            parsed_equation = sp.sympify(eq.split("=")[0]) - sp.sympify(eq.split("=")[1])

            if y in parsed_equation.free_symbols:
                y_vals = [sp.solve(parsed_equation.subs(x, val), y)[0] for val in x_vals]
                plt.plot(x_vals, y_vals, label=f"Equation {i+1}: {eq.strip()}", color=colors[i % len(colors)])
            else:
                y_vals = [parsed_equation.subs(x, val) for val in x_vals]
                plt.plot(x_vals, y_vals, label=f"Equation {i+1}: {eq.strip()}", color=colors[i % len(colors)])

        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Graph of the Equation(s)")
        plt.legend()
        plt.grid()

        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        return base64.b64encode(img.getvalue()).decode()
    except Exception as e:
        return None

# Generate graph explanation
def generate_graph_explanation(equation):
    try:
        prompt = f"Explain the shape and intersection of the graph for the equations: {equation}"
        response = llm.invoke(prompt)
        return response.content if hasattr(response, "content") else str(response)
    except Exception as e:
        return "Error generating graph explanation."

@app.route("/", methods=["GET", "POST"])
def index():
    if "result" not in session:
        session["result"] = None
    if "equation_result" not in session:
        session["equation_result"] = None
    if "graph_img" not in session:
        session["graph_img"] = None
    if "graph_explanation" not in session:
        session["graph_explanation"] = None

    if request.method == "POST":
        if "expression" in request.form:
            expression = request.form["expression"]
            session["result"] = solve_expression(expression)

        if "equation" in request.form:
            equation = request.form["equation"]
            session["equation_result"] = solve_equation(equation)

            if "Error" not in session["equation_result"]:
                session["graph_img"] = generate_graph(equation)
                session["graph_explanation"] = generate_graph_explanation(equation)

    return render_template("index.html", result=session["result"], equation_result=session["equation_result"], graph_img=session["graph_img"], graph_explanation=session["graph_explanation"])

if __name__ == "__main__":
    app.run(debug=True)
