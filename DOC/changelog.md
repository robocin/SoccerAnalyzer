
# Changelog
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased]
- VSS log implementation
- SSL log implementation
- Events class

## [0.3.7] - 2020-08-02

## Added

- Ball positions continuous heatmap

## [0.3.6] - 2020-07-27

## Added

- Category selector
- Log selector

## [0.3.5] - 2020-07-23

## Modified

- Data Collector all statistics initialization

## [0.3.4] - 2020-06-21

## Modified

- Variables, class names and function names developed by the team are now padronized by PEP 8
- Actions accomplished by the team are now called "scored" instead of "made" for clarity purposes
- The data frame used to collect data is now called "game_info" instead of "DataCollector" for clarity purposes

## [0.3.3] - 2020-06-18

## Added

- Teams now have a attribute called "free kicks".

## Modified 

- The information gathered from the data frame is now collected with DataCollector with a top-down approach. 
- Faults, Goals, Penalty or any other event can now be generalizated by the Event class.
- The discrete number of faults and goals is now obtained using Pandas instead of custom functions

## [0.3.2] - 2020-06-04

## Added

- getMostRecentTacklerAndPosition function implementation
- statChanged function implementation
- computeAllGoals implementation
- plotBarData class "data structure" implementation

## Modified

- Underlying code structure changed to be more oop centered (classes instead of single .py)


## [0.3.1] - 2020-05-25

## Modified

- RoboCIn and Adversary will now be instances of teamClass
- Any type of event can now be instantiated as an eventClass

## Deprecated

- RoboCIn and Adversary classes wont be used anymore
- Penalties and Faults classes wont be used anymore

## [0.3.0] - 2020-05-23
 
### Added
 
- Class diagram implementation
- Bar plot implementation
- Pie plot implementation
- Scatter plot implementation
- Changelog

### Fixed
  
- View desapearing while switching tabs

## Changed

- createPlot() now won't be responsible for collecting the log's data
