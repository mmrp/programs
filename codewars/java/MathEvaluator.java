import java.util.*;
public class MathEvaluator {
	LinkedList<String> output;
	LinkedList<String> operator;
	int pos;
	String operators = "()+-*/%#@";
	static final Map<String, Integer> precedence = 
	new HashMap<String, Integer>()
	{{
		put("(", 0);
		put(")", 0);
		put("+", 1);
		put("-", 1);
		put("*", 2);
		put("/", 2);
		put("#", 3);
		put("@", 3);
	}};
	public MathEvaluator() {
		output  = new LinkedList();
		operator = new LinkedList();
		pos = 0;
		
	}

	public String getDigit(char[] ch) {
		String s = "";
		if (ch[pos] == '-') {
			s += '-';
			pos++;
		}

		while (pos < ch.length && (Character.isDigit(ch[pos]) || ch[pos] == '.'))
			s += ch[pos++];
		return s; 

	}

	public double calculate(String expression) {
		return evaluate(expression);
	}
	public double evaluate(String expression) {
		char[] ch = expression.toCharArray();
		boolean prev_operator = true;
		while (pos < ch.length) {
			if (Character.isDigit(ch[pos]))  {	//handle digits
				output.add(getDigit(ch));
				prev_operator = false;
			} else  if (operators.indexOf(ch[pos]) != -1) {	//operator
				String s = Character.toString(ch[pos]);
				if (prev_operator && ch[pos] == '-') 
					s = "#";
				int cprec = precedence.get(s);

				if (ch[pos] == '(') {
					operator.add(s);
					prev_operator = true;
				} else if (ch[pos] == ')') {
					String op = operator.pollLast();
					while (op.charAt(0) != '(') {
						output.add(op);
						op = operator.pollLast();
					}
				} else  {
					prev_operator = true;
					if (operator.size() > 0 && precedence.get(operator.peekLast()) >= cprec) {
						while (operator.size() > 0 && precedence.get(operator.peekLast()) >= cprec) 
							output.add(operator.pollLast());
					}
					operator.add(s);
				}
				pos++;
			}
			else {
				pos++;
			}
			//System.out.println(operator);
			//System.out.println(output);

		}
		while (operator.size() > 0) {
			output.add(operator.pollLast());
		}
		System.out.println(operator);
		System.out.println(output);

		LinkedList<Double> result = new LinkedList();
		for (String s: output) {
			if (operators.indexOf(s) == -1) {
				result.add(Double.parseDouble(s));
			}
			else {
				double a, b, c;
				b = result.pollLast();
				c = -1;
				switch(s.charAt(0)) {
				case '#':
					c = -b;
					break;
				case '+':
					a = result.pollLast();
					c = a + b;
					break;
				case '-':
					a = result.pollLast();
					c = a - b;
					break;
				case '*':
					a = result.pollLast();
					c = a * b;
					break;
				case '/':
					a = result.pollLast();
					c = a / b;
					break;
				default:
					break;
				}
				result.add(c);
			}
		}
		return result.pollLast();
	}

	public static void main(String[] args) {
		MathEvaluator m = new MathEvaluator();
		System.out.println(m.calculate(args[0]));
	}

}
