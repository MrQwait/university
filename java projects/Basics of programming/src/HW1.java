import java.util.Scanner;
public class HW1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Задача 1
        int pies = 12, pay = pies / 2;
        System.out.println("Задача 1\nВходные данные: "+pies);
        System.out.println("Выходные данные: "+pay);

        //Задача 2
        int hour = 12, minutes = 30, seconds = 44321;
        System.out.println("Задача 2\nВходные данные: "+hour+" "+minutes+" "+seconds);
        if ((hour*60*60+minutes*60) >= seconds) {
            System.out.println("Выходные данные: Успел");
        }
        else {
            System.out.println("Выходные данные: Опоздал");
        }

        //Задача 3
        int a = 1, b = 2, c = 3;
        System.out.println("Задача 3\nВходные данные: "+a+" "+b+" "+c);
        if ((a>b)&(a>c)) {
            System.out.println("Выходные данные: "+a);
        }
        if ((b>a)&(b>c)) {
            System.out.println("Выходные данные: "+b);
        }
        if ((c>b)&(c>a)) {
            System.out.println("Выходные данные: "+c);
        }

        //Задача 4
        int year = 1993;
        System.out.println("Задача 4\nВходные данные: "+year);
        if (year % 4==0) {
            System.out.println("Выходные данные: Да");
        }
        else {
            System.out.println("Выходные данные: Нет");
        }

        //Задача 5
        a = 0;
        b = 2;
        System.out.println("Задача 5\nВходные данные: "+a+" "+b);
        if (a!=0)
            System.out.println("Выходные данные: 1");
        else {
            if ((a==b)&(a==0))
                System.out.println("Выходные данные: inf");
            else {
                if ((a==0)&(b!=0))
                    System.out.println("Выходные данные: 0");
            }
        }

        //Задача 6
        a = 1;
        b = -5;
        c = 6;
        System.out.println("Задача 6\nВходные данные: "+a+" "+b+" "+c);
        int D=b*b-4*a*c;
        if (D==0)
            System.out.println("Выходные данные: 1");
        else {
            if (D>0)
                System.out.println("Выходные данные: 2");
            else {
                if (D<0)
                    System.out.println("Выходные данные: 0");
            }
        }

        //Задача 7
        a = 3;
        b = 4;
        c = 5;
        System.out.println("Задача 7\nВходные данные: "+a+" "+b+" "+c);
        if (a<b+c)
            if (b<c+a)
                if (c<b+a)
                    System.out.println("Выходные данные: Yes");
                else
                    System.out.println("Выходные данные: No");

        //Задача 9
        int k = 2, m = 4, n = 3;
        System.out.println("Задача 9\nВходные данные: "+k+" "+m+" "+n);
        if (k >= n) {
            System.out.println("Выходные данные: "+m*2);
        } else if (n*2 % k == 0){
            System.out.println("Выходные данные: "+m*(n*2/k));
        } else {
            System.out.println("Выходные данные: "+m*(1+(n*2/k)));
        }

        //Задача 10
        //int number = sc.nextInt();
        //System.out.println(number % 10);
        //System.out.println(number / 10);
        //System.out.println("X");
    }
}
