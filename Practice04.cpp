#include <iostream>
#include <climits>
#include <array>
using namespace std;

int main()
{
    /*BMI calculator
    weight(kg) / height(m) * height(m)
    Underweight: < 18.5
    Normal weight: 18.5 - 24.9
    Overweight: > 25
    */
   float weight_kg = 0, weight_lbs = 0, height_m = 0, height_ft = 0, bmi = 0;
   float underweight = 18.5, normalweight = 24.9, overweight = 25;
   cout << "Enter your weight in kg: ";
   cin >> weight_kg;
   cout << "Enter your height in meters: ";
   cin >> height_m;
   
   height_ft = height_m * 3.28084;
   weight_lbs = weight_kg * 2.20462;
   
   bmi = weight_kg / (height_m * height_m);

   if (bmi < underweight)
   {
       cout << "You are underweight" << "\n";
       cout << "Your BMI is: " << bmi << "\n";
       cout << "Your weight in lbs is: " << weight_lbs << "\n";
       cout << "Your height in ft is: " << height_ft << "\n";
   }
   else if bmi > underweight && bmi < normalweight
   {
       cout << "You are normal weight" << "\n";
   }
   else
   {
       cout << "You are overweight" << "\n";
   }

   

   return 0;
}