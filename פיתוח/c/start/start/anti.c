//#include <stdio.h>
//#include <stdlib.h>
//#include <conio.h>
//
//#define MAX_NUM 6
//
//int Guess(int tries, int guess[4], int password, int num1, int num2, int num3, int num4)
//{
//	int try = 0;
//	while (tries > 0)
//	{
//		printf("Write your guess (only 1-6, no ENTER is needed)\n%d guesses left: \n", tries);
//		for (int i = 0; i < 4; i++)
//		{
//			guess[i] = _getch() - '0';
//			printf("%d", guess[i]);
//			if (guess[i] == '\n' || guess[i] < 0 || guess[i] > 6)
//			{
//				i = 0;
//				printf("\nwrong input try again\n");
//				_getch();
//			}
//		}
//		_getch();
//		try = guess[3] + guess[2] * 10 + guess[1] * 100 + guess[0] * 1000;
//		if (try == password)
//		{
//			return 1;
//		}
//		else
//		{
//			tries -= 1;
//			int count = 0;
//			int miss = 0;
//			int pass[4] = { num4, num3, num2, num1 };
//			for (int i = 0; i < 4; i++)
//			{
//				if (guess[i] == pass[i])
//				{
//					count++;
//				}
//				else
//					miss++;
//			}
//			printf("\nyou got %d hits and %d misses", count, miss);
//			getchar();
//		}
//
//	}
//	return 0;
//}
//
//
//int main()
//{
//	int num1 = rand() % MAX_NUM + 1;
//	int num2 = rand() % MAX_NUM + 1;
//	int num3 = rand() % MAX_NUM + 1;
//	int num4 = rand() % MAX_NUM + 1;
//	int password = num1 + num2 * 10 + num3 * 100 + num4 * 1000;
//
//	int choice = 0;
//	int guess[4] = { 0 };
//	printf("%d", password);
//	printf("Please choose the game level:\n1 - Easy (20 rounds)\n2 - Moderate (15 rounds)\n3 - Hard (10 rounds)\n4 - Crazy (random number of rounds 5-25)\nMake a choice:");
//	scanf("%d", &choice);
//	getchar();
//	printf("%d\n", password);
//	switch (choice)
//	{
//	case 1:
//		if (Guess(20, guess, password, num1, num2, num3, num4) == 1)
//		{
//			printf("\nwin!!!");
//			break;
//		}
//	case 2:
//		if (Guess(15, guess, password, num1, num2, num3, num4) == 1)
//		{
//			printf("\nwin!!!");
//			break;
//		}
//	case 3:
//		if (Guess(10, guess, password, num1, num2, num3, num4) == 1)
//		{
//			printf("\nwin!!!");
//			break;
//		}
//	case 4:
//		if (Guess((rand() % 25 + 5), guess, password, num1, num2, num3, num4) == 1)
//		{
//			printf("\nwin!!!");
//			break;
//		}
//	}
//
//	return 0;
//}