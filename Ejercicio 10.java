import java.util.Scanner;

class Ejer10{
static Scanner input = new Scanner (System.in);
public static void main (String[] args){

int puntos_acumulados;
int monto_del_salario;

System.out.println("¿puntos acumulados?");
puntos_acumulados=input.nextInt();

System.out.println("¿cual es el monto del salario?");
monto_del_salario=input.nextInt();

if (puntos_acumulados>0 && puntos_acumulados<100) { 
System.out.println("1 salario bono: "+monto_del_salario*1);
}
if (puntos_acumulados>101 && puntos_acumulados<151) {
System.out.println("2 salario bonos: "+monto_del_salario*2);
}
if (puntos_acumulados>151){
System.out.println("3 salario bonos: "+monto_del_salario*3);
}
}
}