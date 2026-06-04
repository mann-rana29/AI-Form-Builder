from pydantic import BaseModel, Field
from typing import Optional, Any, Union, Literal


class BaseElement(BaseModel):
    id: str
    elementType: str


class BaseProps(BaseModel):
    label: str
    required: bool = False
    hidden: bool = False
    width: int = 100


class FullNameProps(BaseProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    minLength: int = 0
    maxLength: int = 100
    autocomplete: str = ""


class FullNameElement(BaseElement):
    elementType: Literal["full-name"]
    props: FullNameProps


class EmailProps(BaseProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    minLength: int = 0
    maxLength: int = 100
    autocomplete: str = ""


class EmailElement(BaseElement):
    elementType: Literal["email"]
    props: EmailProps


class PhoneProps(BaseProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    minLength: int = 0
    maxLength: int = 20
    autocomplete: str = ""
    enableCountryPicker: bool = True
    countryCode: str = "+1"
    validatePhone: bool = False


class PhoneElement(BaseElement):
    elementType: Literal["phone"]
    props: PhoneProps


class MultiLineProps(BaseProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    rows: int = 5
    minLength: int = 0
    maxLength: int = 2000


class MultiLineElement(BaseElement):
    elementType: Literal["multi-line"]
    props: MultiLineProps


class DateOfBirthProps(BaseProps):
    queryKey: str


class DateOfBirthElement(BaseElement):
    elementType: Literal["date-of-birth"]
    props: DateOfBirthProps


class FileUploadProps(BaseProps):
    multiple: bool = False
    maxSize: int = 10
    allowedTypes: str = "*"


class FileUploadElement(BaseElement):
    elementType: Literal["file-upload"]
    props: FileUploadProps


class RatingProps(BaseProps):
    maxRating: int = 5


class RatingElement(BaseElement):
    elementType: Literal["rating"]
    props: RatingProps


class ButtonProps(BaseModel):
    label: str
    fullWidth: bool = False
    align: str = "center"
    subText: str = ""
    customWidth: str = ""
    fontFamily: str = "System UI"
    fontSize: int = 14
    fontWeight: int = 600
    textColor: str = "#ffffff"
    bgColor: str = "#3b82f6"
    borderWidth: int = 0
    borderStyle: str = "solid"
    borderColor: str = "#3b82f6"
    borderRadius: int = 8
    padTop: int = 12
    padRight: int = 24
    padBottom: int = 12
    padLeft: int = 24
    shadowX: int = 0
    shadowY: int = 2
    shadowBlur: int = 4
    shadowSpread: int = 0
    shadowColor: str = "rgba(0,0,0,0.1)"


class ButtonElement(BaseElement):
    elementType: Literal["button"]
    props: ButtonProps


CanvasElement = Union[
    FullNameElement,
    EmailElement,
    PhoneElement,
    MultiLineElement,
    DateOfBirthElement,
    FileUploadElement,
    RatingElement,
    ButtonElement
]



class ImageSchema(BaseModel):
    file: Optional[Any] = None
    url: str = ""


class UiStateSchema(BaseModel):

    is_previewing: bool = Field(
        default=False,
        alias="isPreviewing"
    )

    canvas_view: str = Field(
        default="desktop",
        alias="canvasView"
    )

    canvas_columns: int = Field(
        default=1,
        alias="canvasColumns"
    )

    field_spacing: int = Field(
        default=16,
        alias="fieldSpacing"
    )

    label_alignment: str = Field(
        default="left",
        alias="labelAlignment"
    )

    show_label: bool = Field(
        default=True,
        alias="showLabel"
    )

    input_style: str = Field(
        default="box",
        alias="inputStyle"
    )

    form_width: int = Field(
        default=650,
        alias="formWidth"
    )

    label_width: int = Field(
        default=100,
        alias="labelWidth"
    )

    padding_top: int = Field(
        default=40,
        alias="paddingTop"
    )

    padding_right: int = Field(
        default=40,
        alias="paddingRight"
    )

    padding_bottom: int = Field(
        default=30,
        alias="paddingBottom"
    )

    padding_left: int = Field(
        default=40,
        alias="paddingLeft"
    )

    background_color: str = Field(
        default="#ffffff",
        alias="backgroundColor"
    )

    font_color: str = Field(
        default="#000000",
        alias="fontColor"
    )

    input_background_color: str = Field(
        default="#FFFFFF",
        alias="inputBackgroundColor"
    )

    background_image: ImageSchema = Field(
        default_factory=ImageSchema,
        alias="backgroundImage"
    )

    header_image: ImageSchema = Field(
        default_factory=ImageSchema,
        alias="headerImage"
    )

    border_width: int = Field(
        default=1,
        alias="borderWidth"
    )

    corner_radius: int = Field(
        default=4,
        alias="cornerRadius"
    )

    border_color: str = Field(
        default="#D3D3D3",
        alias="borderColor"
    )

    border_style: str = Field(
        default="solid",
        alias="borderStyle"
    )

    shadow_color: str = Field(
        default="#00000020",
        alias="shadowColor"
    )

    shadow_horizontal: int = Field(
        default=0,
        alias="shadowHorizontal"
    )

    shadow_vertical: int = Field(
        default=2,
        alias="shadowVertical"
    )

    shadow_blur: int = Field(
        default=8,
        alias="shadowBlur"
    )

    shadow_spread: int = Field(
        default=0,
        alias="shadowSpread"
    )

    input_font_color: str = Field(
        default="#000000",
        alias="inputFontColor"
    )

    active_tag_color: str = Field(
        default="#2563EB",
        alias="activeTagColor"
    )

    input_border_width: int = Field(
        default=1,
        alias="inputBorderWidth"
    )

    input_border_color: str = Field(
        default="#D3D3D3",
        alias="inputBorderColor"
    )

    input_corner_radius: int = Field(
        default=10,
        alias="inputCornerRadius"
    )

    input_width: str = Field(
        default="100%",
        alias="inputWidth"
    )

    input_border_style: str = Field(
        default="solid",
        alias="inputBorderStyle"
    )

    input_padding_top: int = Field(
        default=12,
        alias="inputPaddingTop"
    )

    input_padding_right: int = Field(
        default=12,
        alias="inputPaddingRight"
    )

    input_padding_bottom: int = Field(
        default=12,
        alias="inputPaddingBottom"
    )

    input_padding_left: int = Field(
        default=12,
        alias="inputPaddingLeft"
    )

    input_shadow_color: str = Field(
        default="#00000010",
        alias="inputShadowColor"
    )

    input_shadow_horizontal: int = Field(
        default=0,
        alias="inputShadowHorizontal"
    )

    input_shadow_vertical: int = Field(
        default=1,
        alias="inputShadowVertical"
    )

    input_shadow_blur: int = Field(
        default=4,
        alias="inputShadowBlur"
    )

    input_shadow_spread: int = Field(
        default=0,
        alias="inputShadowSpread"
    )

    label_color: str = Field(
        default="#000000",
        alias="labelColor"
    )

    label_font_family: str = Field(
        default="Open Sans",
        alias="labelFontFamily"
    )

    label_font_size: int = Field(
        default=14,
        alias="labelFontSize"
    )

    label_font_weight: int = Field(
        default=400,
        alias="labelFontWeight"
    )

    short_label_color: str = Field(
        default="#666666",
        alias="shortLabelColor"
    )

    short_label_font_family: str = Field(
        default="Open Sans",
        alias="shortLabelFontFamily"
    )

    short_label_font_size: int = Field(
        default=12,
        alias="shortLabelFontSize"
    )

    short_label_font_weight: int = Field(
        default=400,
        alias="shortLabelFontWeight"
    )

    placeholder_color: str = Field(
        default="#74797B",
        alias="placeholderColor"
    )

    placeholder_font_family: str = Field(
        default="Noto Sans JP",
        alias="placeholderFontFamily"
    )

    placeholder_font_size: int = Field(
        default=14,
        alias="placeholderFontSize"
    )

    placeholder_font_weight: int = Field(
        default=400,
        alias="placeholderFontWeight"
    )

    class Config:
        populate_by_name = True