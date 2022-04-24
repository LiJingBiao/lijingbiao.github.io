---
layout: post
title: 批量删除过期描述文件
date: 2022-04-24
tags: iOS
---

`ProvisioningProfile.h`文件
```
#import <Foundation/Foundation.h>

@interface ProvisioningProfile : NSObject

- (id)initWithPath:(NSString *)path;

@property (nonatomic, strong, readonly) NSString    *name;
@property (nonatomic, strong, readonly) NSString    *teamName;
@property (nonatomic, strong, readonly) NSString    *valid;
@property (nonatomic, assign, readonly) NSString    *debug;
@property (nonatomic, strong, readonly) NSDate      *creationDate;
@property (nonatomic, strong, readonly) NSDate      *expirationDate;
@property (nonatomic, strong, readonly) NSString    *UUID;
@property (nonatomic, strong, readonly) NSArray     *devices;
@property (nonatomic, assign, readonly) NSInteger   timeToLive;
@property (nonatomic, strong, readonly) NSString    *applicationIdentifier;
@property (nonatomic, strong, readonly) NSString    *bundleIdentifier;
@property (nonatomic, strong, readonly) NSArray     *certificates;
@property (nonatomic, assign, readonly) NSInteger   version;
@property (nonatomic, assign, readonly) NSArray     *prefixes;
@property (nonatomic, strong, readonly) NSString    *appIdName;
@property (nonatomic, strong, readonly) NSString    *teamIdentifier;
@property (nonatomic, strong, readonly) NSString    *path;

@end

```
`ProvisioningProfile.m`文件
```
#import "ProvisioningProfile.h"

@interface ProvisioningProfile ()

@property (nonatomic, strong) NSDictionary *profileDictionary;
@property (readwrite) NSString  *name;
@property (readwrite) NSString  *teamName;
@property (readwrite) NSString  *valid;
@property (readwrite) NSString  *debug;
@property (readwrite) NSDate    *creationDate;
@property (readwrite) NSDate    *expirationDate;
@property (readwrite) NSString  *UUID;
@property (readwrite) NSArray   *devices;
@property (readwrite) NSInteger timeToLive;
@property (readwrite) NSString  *applicationIdentifier;
@property (readwrite) NSString  *bundleIdentifier;
@property (readwrite) NSArray   *certificates;
@property (readwrite) NSInteger version;
@property (readwrite) NSArray   *prefixes;
@property (readwrite) NSString  *appIdName;
@property (readwrite) NSString  *teamIdentifier;
@property (readwrite) NSString  *path;

@end

@implementation ProvisioningProfile

- (id)initWithPath:(NSString *)path
{
    self = [super init];
    if (self) {
        self.path = path;
        self.profileDictionary = [self provisioningProfileAtPath:path];
        [self processDictionary];
    }
    return self;
}

- (void)processDictionary
{
    self.appIdName = self.profileDictionary[@"AppIDName"];
    self.teamIdentifier = self.profileDictionary[@"Entitlements"][@"com.apple.developer.team-identifier"];
    self.name = self.profileDictionary[@"Name"];
    self.teamName = self.profileDictionary[@"TeamName"];
    self.debug = [self.profileDictionary[@"Entitlements"][@"get-task-allow"] isEqualToNumber:@(1)] ? @"YES" : @"NO";
    self.creationDate = self.profileDictionary[@"CreationDate"];
    self.expirationDate = self.profileDictionary[@"ExpirationDate"];
    self.devices = self.profileDictionary[@"ProvisionedDevices"];
    self.timeToLive = [self.profileDictionary[@"TimeToLive"] integerValue];
    self.applicationIdentifier = self.profileDictionary[@"Entitlements"][@"application-identifier"];
    self.certificates = self.profileDictionary[@"DeveloperCertificates"];
    self.valid = ([[NSDate date] timeIntervalSinceDate:self.expirationDate] > 0) ? @"NO" : @"YES";
    self.version = [self.profileDictionary[@"Version"] integerValue];
    self.bundleIdentifier = self.applicationIdentifier;
    self.UUID = self.profileDictionary[@"UUID"];
    self.prefixes = self.profileDictionary[@"ApplicationIdentifierPrefix"];
    
    for (NSString *prefix in self.prefixes) {
        NSRange range = [self.bundleIdentifier rangeOfString:prefix];
        if (range.location != NSNotFound)
        {
            self.bundleIdentifier = [self.bundleIdentifier stringByReplacingOccurrencesOfString:[NSString stringWithFormat:@"%@.", prefix] withString:@""];
        }
    }
    
}

- (NSDictionary *)provisioningProfileAtPath:(NSString *)path {
    CMSDecoderRef decoder = NULL;
    CFDataRef dataRef = NULL;
    NSString *plistString = nil;
    NSDictionary *plist = nil;
    
    @try {
        CMSDecoderCreate(&decoder);
        NSData *fileData = [NSData dataWithContentsOfFile:path];
        CMSDecoderUpdateMessage(decoder, fileData.bytes, fileData.length);
        CMSDecoderFinalizeMessage(decoder);
        CMSDecoderCopyContent(decoder, &dataRef);
        plistString = [[NSString alloc] initWithData:(__bridge NSData *)dataRef encoding:NSUTF8StringEncoding];
        NSData *plistData = [plistString dataUsingEncoding:NSUTF8StringEncoding];
        
        plist = [NSPropertyListSerialization propertyListWithData:plistData options:NSPropertyListImmutable format:nil error:nil];
    }
    @catch (NSException *exception) {
        NSLog(@"Could not decode file.\n");
    }
    @finally {
        if (decoder) CFRelease(decoder);
        if (dataRef) CFRelease(dataRef);
    }
    
    return plist;
}

@end

```

`main.m`文件
```
//
//  main.m
//  ProvisioningHelper
//
//  Created by lijingbiao on 2022/4/24.
//
#import <AppKit/AppKit.h>
#import "ProvisioningProfile.h"
#import <Foundation/Foundation.h>
static const NSString *kMobileprovisionDirName = @"Library/MobileDevice/Provisioning Profiles";

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSFileManager *manager = [NSFileManager defaultManager];
        NSString *ProvisioningPath = [NSString stringWithFormat:@"%@/%@", NSHomeDirectory(), kMobileprovisionDirName];
        [[NSWorkspace sharedWorkspace]openURL:[NSURL fileURLWithPath:ProvisioningPath]];
        NSLog(@"描述文件路径:%@",ProvisioningPath);
        NSArray *provisionExtensions = @[@"mobileprovision", @"provisionprofile"];
        NSArray *provisioningProfiles = [manager contentsOfDirectoryAtPath:[NSString stringWithFormat:@"%@/%@", NSHomeDirectory(), kMobileprovisionDirName] error:nil];
        provisioningProfiles = [provisioningProfiles filteredArrayUsingPredicate:[NSPredicate predicateWithFormat:@"pathExtension IN %@", provisionExtensions]];
        
        NSMutableArray *provisioningArray = @[].mutableCopy;
        [provisioningProfiles enumerateObjectsUsingBlock:^(id obj, NSUInteger idx, BOOL *stop) {
            NSString *path = (NSString*)obj;
            BOOL isDirectory;
            if ([manager fileExistsAtPath:[NSString stringWithFormat:@"%@/%@/%@", NSHomeDirectory(), kMobileprovisionDirName, path] isDirectory:&isDirectory]) {
                ProvisioningProfile *profile = [[ProvisioningProfile alloc] initWithPath:[NSString stringWithFormat:@"%@/%@/%@", NSHomeDirectory(), kMobileprovisionDirName, path]];
                
                [provisioningArray addObject:profile];
            }
        }];
        for (ProvisioningProfile *profile in provisioningArray) {
            if ([profile.valid isEqualToString:@"NO"] && [manager fileExistsAtPath:profile.path]) {
                NSDateFormatter*formatter =[[NSDateFormatter alloc]init];
                [formatter setDateFormat:@"yyyy-MM-dd"];
                NSString*expirationDate =[formatter stringFromDate:profile.expirationDate];
                NSLog(@"描述文件：%@已过期,过期日期:%@",profile.name,expirationDate);
                NSError *error;
                [manager removeItemAtPath:profile.path error:&error];
                if (error) {
                    NSLog(@"%@删除失败:%@",profile.name,error);
                }else {
                    NSLog(@"%@已删除",profile.name);
                }
            }
        }

    }
    return 0;
}

```
