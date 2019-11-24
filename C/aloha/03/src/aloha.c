// https://www.theurbanpenguin.com/using-getopt-parse-arguments-c/

#include <stdio.h>
#include <getopt.h>

int main ( int argc, char **argv) {
 int option_index = 0;
 char *user_name = NULL;

 while (( option_index = getopt(argc, argv, "u:g")) != -1){
   switch (option_index) {
     case 'u':
      user_name = optarg;
       printf("User is selected\n");
       printf("The user is %s\n",user_name);
       break;
     case 'g':
       printf("Group is selected\n");
       break;
     default:
      printf("Option incorrect\n");
      return 1;
   } //end block for switch
 }  //end block for while

 return 0;
} // end main block
