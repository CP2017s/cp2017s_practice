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
  }

  protected void calculate(){
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


class Unit_Advanced extends Unit{
  private boolean isCmp;
  private String cmp;
  private boolean cmp_result;


  public Unit_Advanced(boolean isCmp, int left, int right, String arg){
    super(left,right,' ');
    this.isCmp = isCmp;
    if(isCmp){
      cmp=arg;
    }
    else{
      type = arg.charAt(0);
    }
  }

  protected void calculate(){
    switch(type){
      case '+':
      case '-':
      case '/':
      case '%':
      case '*':
        super.calculate();
        break;
      case '^':
        this.result = (int) Math.pow(this.left,this.right);
        break;
      case '&':
        this.result = this.left & this.right;
        break;
      case '|':
        this.result = this.left | this.right;
        break;
      case '>':
        this.result = this.left >> this.right;
        break;
      case '<':
        this.result = this.left << this.right;
        break;
    }
  }


  private void compare(){
    switch(cmp){
      case ">":
        this.cmp_result=(left>right);
        break;
      case ">=":
        this.cmp_result=(left>=right);
        break;
      case "<":
        this.cmp_result=(left<right);
        break;
      case "<=":
        this.cmp_result=(left<=right);
        break;
      case "==":
        this.cmp_result=(left==right);
        break;
      case "!=":
        this.cmp_result=(left!=right);
        break;
    }
  }


  public void run(){
    if(isCmp)
      compare();
    else
      calculate();
  }
  public String toString(){
    if(isCmp){
      return Integer.toString(left)+cmp+Integer.toString(right)+" : "+cmp_result;
    }
    else{
      return super.toString();
    }
  }
}

public class ex5_2{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String input = "";
    while(!(input = br.readLine()).equals("QUIT")){
      String[] parsed = input.split(" ");
      boolean iscmp=false;
      if(parsed[0].equals("cmp"))
        iscmp=true;

      int l = Integer.parseInt(parsed[1]);
      int r = Integer.parseInt(parsed[2]);
      Unit_Advanced ua = new Unit_Advanced(iscmp,l,r,parsed[3]);
      ua.run();
      System.out.println(ua.toString());
    }
    return;   
  }
}


