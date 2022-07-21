# compile_commands.json
```
"D:\Games\UE_5.0\Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.exe" -mode=GenerateClangDatabase -project=d:\projects\eins\eins.uproject eins Development Win64
```

# Diff
```
UE4Editor.exe ${projectpath} -diff %1 %2
```

# Unreal Insights
```
-tracehost=10.0.254.35 -trace=memory,log,frame,cpu
```

# Misc
```
stat fps
stat unit
E:/g2/UE4/Engine/Binaries/Win64/UE4Editor.exe E:/path/to/uproject -run=DerivedDataCache -fill -DDC=CreatePak
Command line: -ExecCmds="stat unit" -LogCmds="LogOnlineVoice verbose"
```

# .lvimrc
```
set shiftwidth=4
set tabstop=4
set softtabstop=4

if &ft == "cpp"
  setlocal noexpandtab
endif

if &ft == "cs"
  setlocal noexpandtab
endif

noremap <F9> :terminal ++shell D:/projects/UnrealEngine/Engine/Build/BatchFiles/Build.bat MyProject Win64 Development D:/projects/MyProject/MyProject.uproject -waitmutex<CR>
"noremap <F9> :terminal ++shell D:/projects/UnrealEngine/Engine/Build/BatchFiles/Build.bat MyProjectEditor Win64 Development D:/projects/MyProject/MyProject.uproject -waitmutex<CR>
```

# .gitignore
```
# ignore everything
*
# except folders
!*/
# and files with these extensions
!*.bff
!*.c
!*.cc
!*.cpp
!*.h
!*.hpp
!*.inl
!*.cs

# but not in this folder
**/ThirdParty*
**/Intermediate*
```

# .gutctags
```
--languages=C++,C#
--exclude=ThirdParty
--exclude=Intermediate
-D UPROPERTY()=
-D UFUNCTION()=
-D DECLARE_EVENT( OwningType, EventName )=typedef A EventName;
-D DECLARE_EVENT_OneParam( OwningType, EventName, Param1Type )=typedef A EventName;
-D DECLARE_DELEGATE( DelegateName )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE( DelegateName )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE( DelegateName )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE( DelegateName )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal( ReturnValueType, DelegateName )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal( ReturnValueType, DelegateName )=typedef A DelegateName;
-D DECLARE_DELEGATE_OneParam( DelegateName, Param1Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_OneParam( DelegateName, Param1Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_OneParam( DelegateName, Param1Type, Param1Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam( DelegateName, Param1Type, Param1Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_OneParam( ReturnValueType, DelegateName, Param1Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam( ReturnValueType, DelegateName, Param1Type, Param1Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_TwoParams( DelegateName, Param1Type, Param2Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_TwoParams( DelegateName, Param1Type, Param2Type )=typedef A DelegateName;
-D DECLARE_EVENT_TwoParams( OwningType, EventName, Param1Type, Param2Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_TwoParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_TwoParams( ReturnValueType, DelegateName, Param1Type, Param2Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_TwoParams( ReturnValueType, DelegateName, Param1Type, Param1Name, Param2Type, Param2Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_ThreeParams( DelegateName, Param1Type, Param2Type, Param3Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_ThreeParams( DelegateName, Param1Type, Param2Type, Param3Type )=typedef A DelegateName;
-D DECLARE_EVENT_ThreeParams( OwningType, EventName, Param1Type, Param2Type, Param3Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_ThreeParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_ThreeParams( ReturnValueType, DelegateName, Param1Type, Param2Type, Param3Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_ThreeParams( ReturnValueType, DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_FourParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_FourParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type )=typedef A DelegateName;
-D DECLARE_EVENT_FourParams( OwningType, EventName, Param1Type, Param2Type, Param3Type, Param4Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_FourParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_FourParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_FourParams( ReturnValueType, DelegateName, Param1Type, Param2Type, Param3Type, Param4Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_FourParams( ReturnValueType, DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_FiveParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_FiveParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type )=typedef A DelegateName;
-D DECLARE_EVENT_FiveParams( OwningType, EventName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_FiveParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_FiveParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_FiveParams( ReturnValueType, DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_FiveParams( ReturnValueType, DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_SixParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_SixParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type )=typedef A DelegateName;
-D DECLARE_EVENT_SixParams( OwningType, EventName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_SixParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_SixParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_SixParams( ReturnValueType, DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_SixParams( ReturnValueType, DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_SevenParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_SevenParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type )=typedef A DelegateName;
-D DECLARE_EVENT_SevenParams( OwningType, EventName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_SevenParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_SevenParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_SevenParams( ReturnValueType, DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_SevenParams( ReturnValueType, DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_EightParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type, Param8Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_EightParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type, Param8Type )=typedef A DelegateName;
-D DECLARE_EVENT_EightParams( OwningType, EventName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type, Param8Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_EightParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name, Param8Type, Param8Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_EightParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name, Param8Type, Param8Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_EightParams( ReturnValueType, DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type, Param8Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_EightParams( ReturnValueType, DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name, Param8Type, Param8Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_NineParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type, Param8Type, Param9Type )=typedef A DelegateName;
-D DECLARE_MULTICAST_DELEGATE_NineParams( DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type, Param8Type, Param9Type )=typedef A DelegateName;
-D DECLARE_EVENT_NineParams( OwningType, EventName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type, Param8Type, Param9Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_NineParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name, Param8Type, Param8Name, Param9Type, Param9Name )=typedef A DelegateName;
-D DECLARE_DYNAMIC_MULTICAST_DELEGATE_NineParams( DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name, Param8Type, Param8Name, Param9Type, Param9Name )=typedef A DelegateName;
-D DECLARE_DELEGATE_RetVal_NineParams( ReturnValueType, DelegateName, Param1Type, Param2Type, Param3Type, Param4Type, Param5Type, Param6Type, Param7Type, Param8Type, Param9Type )=typedef A DelegateName;
-D DECLARE_DYNAMIC_DELEGATE_RetVal_NineParams( ReturnValueType, DelegateName, Param1Type, Param1Name, Param2Type, Param2Name, Param3Type, Param3Name, Param4Type, Param4Name, Param5Type, Param5Name, Param6Type, Param6Name, Param7Type, Param7Name, Param8Type, Param8Name, Param9Type, Param9Name )=typedef A DelegateName;
```
