package colormixingSystem;

import java.util.Scanner;

public class colorMixer {

	public static void main(String[] args) {
		
		String red = "red";
		String blue = "blue";
		String yellow = "yellow";
		
		Scanner input = new Scanner(System.in);
		System.out.println("Enter primary color (red, blue, yellow):");
		String p1 = input.nextLine();
		System.out.println("Enter another primary color(red, blue, yellow):");
		String p2 = input.nextLine();
		
		
		
		if( (p1.equals(red)) & (p2.equals(blue))) {
			System.out.println("When you mix red and blue, you get purple");
		}
		else if( (p1.equals(red)) & (p2.equals(yellow))) {
			System.out.println("When you mix red and yellow, you get orange");
		}
		else if( (p1.equals(red)) & (p2.equals(red))) {
			System.out.println("When you mix red and red, you get red");
		}
		else if((p1.equals(blue)) & (p2.equals(red))) {
			System.out.println("When you mix blue and red, you get purple");
		}
		else if( (p1.equals(blue)) & (p2.equals(yellow))) {
			System.out.println("When you mix blue and yellow, you get green");
		}
		else if ( (p1.equals(blue)) & (p2.equals(blue))) {
			System.out.println("When you mix blue and blue,you get blue");
		}
		
		else if ((p1.equals(yellow)) & (p2.equals(red))) {
			System.out.println("When you mix yellow and red, you get orange");
			
		}
		else if (p1.equals(yellow) & (p2.equals(blue))) {
			System.out.println("When you mix yellow and blue, you get green;");
		}
		else if (p1.equals(yellow) & (p2.equals(yellow))) {
			System.out.println("When you mix yellow and yellow, you get yellow");
		}
		else {
			System.out.println("You didn't input two primary colors");
		}
	

	

		

	}

}
