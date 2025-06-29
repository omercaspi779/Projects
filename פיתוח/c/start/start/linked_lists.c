//#include <stdio.h>
//#include <stdlib.h>
//#include <string.h>
//
//#define STR_LEN 15
//
//typedef struct SongNode
//{
//    char name[STR_LEN];
//    char artist[STR_LEN];
//    int duration;
//    struct SongNode* next;
//} SongNode;
//
//SongNode* createSong(char name[], char artist[], int duration);
//void printList(SongNode* head);
//
//int main(void)
//{
//    SongNode* first = NULL;
//    SongNode* second = NULL;
//    SongNode* third = NULL;
//
//    first = createSong("Etze hashuka", "Shefita", 123);
//    second = createSong("Sara", "Bob Dylan", 327);
//    third = createSong("Tziona", "Nisim Gareme", 283);
//
//    first->next = second;
//    second->next = third;
//
//    printList(first);
//
//    SongNode* curr = first;
//    SongNode* temp = NULL;
//    while (curr)
//    {
//        temp = curr->next;
//        free(curr);
//        curr = temp;
//    }
//    first = NULL;
//
//    return 0;
//}
//
///**
//Function will create a song
//input:
//song name, artist name, and its duration
//output:
//the song updated with correct information
//*/
//SongNode* createSong(char name[], char artist[], int duration)
//{
//    SongNode* newSong = (SongNode*)malloc(sizeof(SongNode));
//
//    strncpy(newSong->name, name, STR_LEN);
//    strncpy(newSong->artist, artist, STR_LEN);
//    newSong->duration = duration;
//    newSong->next = NULL;
//
//    return newSong;
//}
//
///**
//Function will print a list of songs
//input: the list (the first song)
//output:
//none
//*/
//void printList(SongNode* head)
//{
//    SongNode* curr = head;
//    printf("Playlist\n");
//    printf("--------\n");
//    while (curr) // when curr == NULL, that is the end of the list, and loop will end (NULL is false)
//    {
//        printf("%s - %s (%d sec)\n", curr->artist, curr->name, curr->duration);
//        curr = curr->next;
//    }
//    printf("\n");