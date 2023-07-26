---
layout: post
title: iOSTextView长度限制
date: 2023-07-26
tags: iOS
---

```
-(void)textViewDidChange:(UITextView *)textView
{
    UITextRange *selectedRange = [textView markedTextRange];
    UITextPosition *position = [textView positionFromPosition:selectedRange.start offset:0];
    if (!position) {
        NSInteger length = [self showLength:textView.text];
        if (length <= _maxLength) {
            self.countWordLabel.text = [NSString stringWithFormat:@"%ld/15",length];
        }
        else {
            // 开始裁减了
            NSString *text = textView.text;
            NSString *tobeString = [text substringToIndex:text.length - 1];
            while ([self showLength:tobeString] > _maxLength) {
                tobeString = [tobeString substringToIndex:tobeString.length - 1];
            }
            textView.text = tobeString;
            self.countWordLabel.text = [NSString stringWithFormat:@"%ld/15",15];
        }
    }
}

-(BOOL)textView:(UITextView *)textView shouldChangeTextInRange:(NSRange)range replacementText:(NSString *)text
{
    UITextRange *selectedRange = [textView markedTextRange];
    UITextPosition *position = [textView positionFromPosition:selectedRange.start offset:0];
    if (!position) {
        if (text.length > 0) {
            if ([self realLength:textView.text] >= _maxLength) {
                return NO;
            }
        }
    }
    return YES;
}
#pragma mark - 长度计算
- (NSInteger)realLength:(NSString *)text
{
    return [self getStringRealLengthWithText:text];
}
- (NSInteger)showLength:(NSString *)text
{
    return [self getStringShowLengthWithText:text];
}
/// 真实长度
- (CGFloat)getStringRealLengthWithText:(NSString *)text
{
    __block CGFloat stringLength = 0.0;
    __weak typeof(self) weakSelf = self;
    [text enumerateSubstringsInRange:NSMakeRange(0, text.length) options:NSStringEnumerationByComposedCharacterSequences usingBlock:^(NSString * _Nullable substring, NSRange substringRange, NSRange enclosingRange, BOOL * _Nonnull stop) {
        //NSLog(@"%@  \t%zd", substring, strlen([substring UTF8String]));
        NSInteger l = strlen([substring UTF8String]);
        /// 表情
        if (l >= 4) stringLength += 1.0;
        /// 汉字
        else if (l == 3) stringLength += 1.0;
        /// 其它
        else stringLength += 1;
    }];
    return stringLength;
}

/// 显示的长度
- (NSInteger)getStringShowLengthWithText:(NSString *)text
                          
{
    CGFloat length = [self getStringRealLengthWithText:text];
    return (NSInteger)roundf(length);
}
```
