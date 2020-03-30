import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.temporal.ChronoUnit;
import java.util.Calendar;
import java.util.Date;

public class Question1 {

    //How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    public static void main(String[] args){

        System.out.println("the loop-based solution = "+loopSolution());

    }

    //uses a loop to find the total number of Sundays
    public static int loopSolution(){

        int numOccour = 0;

        String strDate = "1901-01-01";
        String endDate = "2000-12-31";

        Long millis;
        Date startD = new Date();
        Date endD = new Date();

        //parses given dates into accurate Epoch time measures
        try {
            millis = new SimpleDateFormat("yyyy-MM-dd").parse(strDate).getTime();
            startD = new Date(millis);
            millis = new SimpleDateFormat("yyyy-MM-dd").parse(endDate).getTime();
            endD = new Date(millis);
        } catch (ParseException e) {
            e.printStackTrace();
        }

        if(startD.after(endD)){
            System.out.println("invalid dates");
            return -1;
        }

        Calendar cal = Calendar.getInstance();
        cal.setTime(startD);

        //moves calandar until we reach the appriate weekday to count (sunday in our case)
        while(cal.get(Calendar.DAY_OF_WEEK)!=Calendar.SUNDAY){
            cal.add(Calendar.DATE,1);
        }

        //moves week by week until there dates are invalid, each day is on appropriate weekDay, so we can just count the ones that land on the first of the month
        while(cal.getTime().before(endD)){
            cal.add(Calendar.DATE,7);

            if (cal.get(Calendar.DAY_OF_MONTH)==1){
                numOccour++;
            }

        }

        return numOccour;
    }


}
