 fprintf(file,"%lf, %lf, %lf, %lf, ",detection.ball().x(),detection.ball().y(),detection.ball().vx(),detection.ball().vy());
  for(int i = 0; i < detection.robots_yellow_size();i++){
      fprintf(file,"%lf, %lf, %lf, %lf, %lf, %lf, ", detection.robots_yellow(i).x(),detection.robots_yellow(i).y(),detection.robots_yellow(i).vx(),detection.robots_yellow(i).vy(),detection.robots_yellow(i).orientation(),detection.robots_yellow(i).vorientation());
  }
  for(int i = 0; i < detection.robots_blue_size();i++){
      fprintf(file,"%lf, %lf, %lf, %lf, %lf, %lf, ", detection.robots_blue(i).x(),detection.robots_blue(i).y(),detection.robots_blue(i).vx(),detection.robots_blue(i).vy(),detection.robots_blue(i).orientation(),detection.robots_blue(i).vorientation());
  }
  fprintf(file,"%d, %d, %d, %d, %d, %d, %lf \n",fault, goalShot, penalty, goal, side, faulType, elapsed);
