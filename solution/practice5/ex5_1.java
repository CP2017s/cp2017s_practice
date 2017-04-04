import java.io.*;
import java.util.*;


class Unit{
  int left;
  int right;
  char type;
  int result;


  public Unit(int left, int right,char type){
    this.left=left;
    this.right=right;
    this.type = type;
    calculate();
  }
  private void calculate(){
    switch(type){
      case '+' :
        this.result = this.left + this.right;
        break;
      case '-' :
        this.result = this.left - this.right;
        break;
      case '/' : 
        this.result = this.left / this.right;
        break;
      case '%' :
        this.result = this.left % this.right;
        break;
      case '*' :
        this.result = this.left*this.right;
        break;
    }
  }
  public String toString(){
    if(type == ' ')
      return "No Expression";
    else
      return Integer.toString(left)+type+Integer.toString(right)+"="+Integer.toString(result);
  }
}


public class ex5_1{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String input = "";
    while(!(input = br.readLine()).equals("QUIT")){

      String[] parsed = input.split(" ");
      int l = Integer.parseInt(parsed[0]);
      int r = Integer.parseInt(parsed[1]);
      char t = parsed[2].charAt(0);
      Unit u = new Unit(l,r,t);
      System.out.println(u.toString());
    }
    return;   
  }
}


