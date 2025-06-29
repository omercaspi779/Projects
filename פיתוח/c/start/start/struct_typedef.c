//#include <stdio.h>
//#include <stdlib.h>
//#include <conio.h>
//#include <string.h>
//
//struct animal 
//{
//	char type[30];
//	char name[30];
//	int age;
//};
//
//typedef struct animal animal;
//
//
//void print_animals(animal a)
//{
//	printf("the name is: %s\n", a.name);
//	printf("the type is: %s\n", a.type);
//	printf("the age is: %d\n", a.age);
//}
//
//
//int is_equal(animal a1, animal a2)
//{
//	if (a1.age == a2.age && strcmp(a1.type, a2.type) == 0 && strcmp(a1.name, a2.name) == 0)
//	{
//		return 1;
//	}
//	else
//		return 0;
//}
//
//
//
//int main()
//{
//	animal animal1 = { "", "", 0 };
//	animal animal2 = { "", "", 0 };
//	printf("animal 1 name: ");
//	scanf("%s", &animal1.name);
//	printf("animal 1 type: ");
//	scanf("%s", &animal1.type);
//	printf("animal 1 age: ");
//	scanf("%d", &animal1.age);
//	getchar();
//	printf("animal 2 name: ");
//	scanf("%s", &animal2.name);
//	printf("animal 2 type: ");
//	scanf("%s", &animal2.type);
//	printf("animal 2 age: ");
//	scanf("%d", &animal2.age);
//	getchar();
//	printf("sizeof = %d\n", sizeof(struct animal));
//	print_animals(animal1);
//	print_animals(animal2);
//	int try2 = is_equal(animal1, animal2);
//	printf("if its 1 its true and 0 is false: %d", try2);
//}